# routes/home.py
# Ver 2024.10.6
# For SlamSim

from db import db
from flask import Blueprint, render_template
from models.league import league_model
from flask import current_app as app  
home_routes = Blueprint('home_routes', __name__)

@home_routes.route('/', methods=['GET'])
def index():
    active_leagues = league_model.query.filter_by(status='Active').all()
    return render_template('index.html', leagues=active_leagues)
    