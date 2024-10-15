# routes/leagues.py
# Ver 2024.10.14
# For SlamSim

from db import db
from flask import Blueprint, render_template, redirect, url_for, request
import os, markdown2
from models.league import league_model
from flask import current_app as app
from werkzeug.utils import secure_filename
from forms.league import league_form
league_routes = Blueprint('league_routes', __name__)

@league_routes.route('/leagues/new', methods=['GET', 'POST'], endpoint='create_league')
def create_league():
    form = league_form()
    if form.validate_on_submit():
        
        logo_filename = None
        logo = form.logo.data
        if logo:
            filename = secure_filename(logo.filename)
            logo.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
            logo_filename = filename

        league = league_model(
            name=form.name.data,
            abbreviation=form.abbreviation.data,
            logo=logo_filename,
            status=form.status.data,
            owner=form.owner.data,
            headquarters=form.headquarters.data,
            description=form.description.data
        )

        db.session.add(league)
        db.session.commit()
        return redirect(url_for('league_routes.list_leagues'))
    return render_template('leagues/create.html', form=form)
    
@league_routes.route('/leagues/<int:league_id>')
def view_league(league_id):
    league = league_model.query.get_or_404(league_id)
    description_html = markdown2.markdown(league.description or '')
    print(description_html)
    return render_template('leagues/view.html', league=league, description_html=description_html)
    
@league_routes.route('/leagues/<int:league_id>/edit', methods=['GET', 'POST'])
def edit_league(league_id):
    league = league_model.query.get_or_404(league_id)
    form = league_form(obj=league)
    if form.validate_on_submit():
        if form.logo.data:
            logo_filename = secure_filename(form.logo.data.filename)
            form.logo.data.save(os.path.join(app.config['UPLOAD_FOLDER'], logo_filename))
            league.logo = logo_filename  # Update logo if a new one is uploaded
        
        # Populate other fields except 'logo'
        league.name = form.name.data
        league.abbreviation = form.abbreviation.data
        league.status = form.status.data
        league.headquarters = form.headquarters.data
        league.owner = form.owner.data
        league.description = form.description.data

        db.session.commit()
        return redirect(url_for('league_routes.view_league', league_id=league.id))
    return render_template('leagues/edit.html', form=form, league=league)

@league_routes.route('/leagues', methods=['GET'])
def list_leagues():
    filter_option = request.args.get('filter', 'all')
    if filter_option == 'active':
        leagues = league_model.query.filter_by(status='Active').all()
    elif filter_option == 'inactive':
        leagues = league_model.query.filter_by(status='Inactive').all()
    else:
        leagues = league_model.query.all()
    return render_template('leagues/list.html', leagues=leagues, filter_option=filter_option)
