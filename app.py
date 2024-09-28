import os
from flask import Flask, render_template, request, redirect, flash, url_for
from flask_sqlalchemy import SQLAlchemy
from werkzeug.utils import secure_filename
from models import db, Wrestler, League, TagTeam
from utils.sanitize import sanitize_input, sanitize_limit_html, sanitize_number
from utils.file_upload import save_image
from utils.process_forms import process_wrestler_form, process_tagteam_form, process_league_form

# Flask app setup
app = Flask(__name__)
app.secret_key = 'your_secret_key'

# SQLite database setup
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///slamsim.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db.init_app(app)

# Uploads folder configuration
UPLOAD_FOLDER = 'static/uploads/'
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

# Create folder if it doesn't exist
if not os.path.exists(UPLOAD_FOLDER):
    os.makedirs(UPLOAD_FOLDER)

# Home route

@app.route('/')
def home(): 
    # Retrieve all leagues from the database
    leagues = League.query.all()
    # Pass leagues to the template
    return render_template('home.html', leagues=leagues)

# Wrestler Routes

@app.route('/create_wrestler', methods=['GET', 'POST'])

def create_wrestler():
    leagues = League.query.all()
    if request.method == 'POST':
        try:
            new_wrestler = process_wrestler_form()
            db.session.add(new_wrestler)
            db.session.commit()
            flash('Wrestler created successfully!', 'success')
            return redirect(url_for('home'))
        
        except Exception as e:
            db.session.rollback()
            flash('Error creating wrestler. Please try again.', 'error')
    return render_template('create_wrestler.html', leagues=leagues)

@app.route('/wrestler/<int:id>', methods=['GET', 'POST'])
def view_edit_wrestler(id):
    wrestler = Wrestler.query.get_or_404(id)

    if request.method == 'POST':
        updated_wrestler = process_wrestler_form(wrestler)
        db.session.commit()
        flash('Wrestler updated successfully!', 'success')
        return redirect(url_for('view_edit_wrestler', id=wrestler.id))

    return render_template('view_edit_wrestler.html', wrestler=wrestler)

@app.route('/list_wrestlers', methods=['GET'])
def list_wrestlers():
    # Get filter parameters from the query string
    status_filter = request.args.get('status')
    league_filter = request.args.get('league')

    # Base query
    query = Wrestler.query

    # Apply status filter if specified
    if status_filter:
        query = query.filter_by(status=status_filter)

    # Apply league filter if specified
    if league_filter:
        if league_filter == 'None':
            query = query.filter_by(league_id=None)
        else:
            query = query.filter_by(league_id=league_filter)

    # Get the filtered list of wrestlers
    wrestlers = query.all()

    # Get all leagues for filter options
    leagues = League.query.all()

    return render_template('list_wrestlers.html', wrestlers=wrestlers, leagues=leagues, status_filter=status_filter, league_filter=league_filter)

# Tag-team routes

@app.route('/create_tagteam', methods=['GET', 'POST'])
def create_tagteam():
    leagues = League.query.all()
    wrestlers = Wrestler.query.all()

    if request.method == 'POST':
        process_tagteam_form()
        flash('Tag Team created successfully!', 'success')
        return redirect(url_for('list_tagteams'))

    return render_template('create_tagteam.html', leagues=leagues, wrestlers=wrestlers)

@app.route('/list_tagteams', methods=['GET'])
def list_tagteams():
    status_filter = request.args.get('status')
    league_filter = request.args.get('league')

    query = TagTeam.query

    if status_filter:
        query = query.filter_by(status=status_filter)
    if league_filter:
        query = query.filter_by(league_id=league_filter)

    tagteams = query.all()
    leagues = League.query.all()

    return render_template('list_tagteams.html', tagteams=tagteams, leagues=leagues)

@app.route('/tagteam/<int:id>', methods=['GET', 'POST'])
def view_edit_tagteam(id):
    tagteam = TagTeam.query.get_or_404(id)
    leagues = League.query.all()
    wrestlers = Wrestler.query.all()

    if request.method == 'POST':
        process_tagteam_form(tagteam)
        flash('Tag Team updated successfully!', 'success')
        return redirect(url_for('list_tagteams'))

    return render_template('view_edit_tagteam.html', tagteam=tagteam, leagues=leagues, wrestlers=wrestlers)

@app.route('/create_faction', methods=['GET', 'POST'])
def create_faction():
    if request.method == 'POST':
        # Similar structure for handling faction creation
        flash('Faction created successfully!', 'success')
        return redirect(url_for('home'))
    return render_template('create_faction.html')

@app.route('/create_staff', methods=['GET', 'POST'])
def create_staff():
    if request.method == 'POST':
        # Similar structure for handling staff creation
        flash('Staff member created successfully!', 'success')
        return redirect(url_for('home'))
    return render_template('create_staff.html')

# League routes

@app.route('/create_league', methods=['GET', 'POST'])
def create_league():
    if request.method == 'POST':
        process_league_form()
        flash('League created successfully!', 'success')
        
    return render_template('create_league.html')


@app.route('/create_venue', methods=['GET', 'POST'])
def create_venue():
    if request.method == 'POST':
        # Similar structure for handling venue creation
        flash('Venue created successfully!', 'success')
        return redirect(url_for('home'))
    return render_template('create_venue.html')

# Route to set up the league dashboard

@app.route('/league/<int:league_id>')
def play_league(league_id):
    league = league.query.get_or_404(league_id)

    return render_template('play_league.html', league=league)

# Function to initialize the database
def create_tables():
    db.create_all()

# Main block to run the app and create tables if necessary
if __name__ == '__main__':
    with app.app_context():
        create_tables()  # Create tables within the application context
    app.run(debug=True)
