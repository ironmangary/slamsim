# process_forms helpers
# For SlamSim

from flask import Flask, render_template, request, redirect, flash, url_for
from werkzeug.utils import secure_filename
from utils.sanitize import sanitize_input, sanitize_limit_html, sanitize_number
from utils.file_upload import save_image
from models import db, Wrestler, League, TagTeam

def process_wrestler_form(wrestler_instance=None):
    name = sanitize_input(request.form['name'])
    nickname = sanitize_input(request.form.get('nickname', ''))
    height = sanitize_input(request.form.get('height', ''))
    weight = sanitize_input(request.form.get('weight', ''))
    gender = sanitize_input(request.form['gender'])
    location = sanitize_input(request.form.get('location', ''))   
    league_id = request.form['league']
    if league_id == "None":
        league_id = None
    alignment = sanitize_input(request.form['alignment'])
    style = sanitize_input(request.form['style'])
    card_level = sanitize_input(request.form['card_level'])
    manager = sanitize_input(request.form.get('manager', ''))
    tagteam = sanitize_input(request.form.get('tagteam', ''))
    faction = sanitize_input(request.form.get('faction', ''))
    finisher1 = sanitize_input(request.form['finisher1'])
    finisher2 = sanitize_input(request.form.get('finisher2', ''))
    finisher3 = sanitize_input(request.form.get('finisher3', ''))
    standard1 = sanitize_input(request.form['standard1'])
    standard2 = sanitize_input(request.form['standard2'])
    standard3 = sanitize_input(request.form.get('standard3', ''))
    standard4 = sanitize_input(request.form.get('standard4', ''))
    standard5 = sanitize_input(request.form.get('standard5', ''))
    extreme1 = sanitize_input(request.form.get('extreme1', ''))
    extreme2 = sanitize_input(request.form.get('extreme2', ''))
    extreme3 = sanitize_input(request.form.get('extreme3', ''))
    status = sanitize_input(request.form['status'])
    bio = sanitize_limit_html(request.form.get('bio', ''))

    image = None
    if 'image' in request.files:
        image = request.files['image']
        image_filename = save_image(image)  

    if wrestler_instance is None:
        wrestler_instance = Wrestler(
            name=name, nickname=nickname, height=height, weight=weight, gender=gender,
            location=location, image=image_filename, league_id=league_id,
            alignment=alignment, style=style,
            card_level=card_level, manager=manager, tagteam=tagteam, faction=faction,
            finisher1=finisher1, finisher2=finisher2,
            finisher3=finisher3, standard1=standard1, standard2=standard2,
            standard3=standard3, standard4=standard4, standard5=standard5,
            extreme1=extreme1, extreme2=extreme2, extreme3=extreme3, status=status, bio=bio
        )
    else:
        wrestler_instance.name=name 
        wrestler_instance.nickname=nickname
        wrestler_instance.height=height
        wrestler_instance.weight=weight
        wrestler_instance.gender=gender
        wrestler_instance.location=location
        wrestler_instance.image=image_filename
        wrestler_instance.league_id=league_id
        wrestler_instance.alignment=alignment
        wrestler_instance.style=style
        wrestler_instance.card_level=card_level
        wrestler_instance.manager=manager
        wrestler_instance.tagteam=tagteam
        wrestler_instance.faction=faction
        wrestler_instance.finisher1=finisher1
        wrestler_instance.finisher2=finisher2
        wrestler_instance.finisher3=finisher3
        wrestler_instance.standard1=standard1
        wrestler_instance.standard2=standard2
        wrestler_instance.standard3=standard3
        wrestler_instance.standard4=standard4
        wrestler_instance.standard5=standard5
        wrestler_instance.extreme1=extreme1
        wrestler_instance.extreme2=extreme2
        wrestler_instance.extreme3=extreme3
        wrestler_instance.status=status
        wrestler_instance.bio=bio
    return wrestler_instance

def process_league_form(league_instance=None):
    name = sanitize_input(request.form['name'])
    abbreviation = sanitize_input(request.form['abbreviation'])
    status = sanitize_input(request.form['status'])
    headquarters = sanitize_input(request.form.get('headquarters', ''))
    owner = sanitize_input(request.form.get('owner', ''))
    year_created = sanitize_number(request.form['year_created'], allow_empty=True)
    description = sanitize_limit_html(request.form.get('description', ''))

    if league_instance is None:
        league_instance = League(
            name=name, abbreviation=abbreviation, status=status,
            headquarters=headquarters, owner=owner, year_created=year_created, description=description
        )
        db.session.add(league_instance)
    else:
        league_instance.name = name
        league_instance.abbreviation = abbreviation
        league_instance.status = status
        league_instance.headquarters = headquarters
        league_instance.owner = owner
        league_instance.year_created = year_created
        league_instance.description = description
    db.session.commit()
    return league_instance


def process_tagteam_form(tagteam_instance=None):
    name = sanitize_input(request.form['name'])
    tagteam_type = sanitize_input(request.form['type'])
    gender = sanitize_input(request.form['gender'])
    league_id = request.form['league']
    if league_id == "None":
        league_id = None
    wrestler1_id = request.form.get('wrestler1')
    wrestler2_id = request.form.get('wrestler2')
    wrestler3_id = request.form.get('wrestler3') if tagteam_type == 'trios' else None
    manager = sanitize_input(request.form.get('manager'))
    finisher1 = sanitize_input(request.form.get('finisher1'))
    finisher2 = sanitize_input(request.form.get('finisher2'))
    finisher3 = sanitize_input(request.form.get('finisher3'))
    status = sanitize_input(request.form.get('status', 'active'))
    bio = sanitize_limit_html(request.form.get('bio'))
    
    if not tagteam:
        tagteam = TagTeam(
            name=name,
            type=tagteam_type,
            gender=gender,
            league_id=league_id,
            wrestler1_id=wrestler1_id,
            wrestler2_id=wrestler2_id,
            wrestler3_id=wrestler3_id,
            manager=manager,
            finisher1=finisher1,
            finisher2=finisher2,
            finisher3=finisher3,
            bio=bio,
            status=status
        )
        db.session.add(tagteam)
    else:
        tagteam.name = name
        tagteam.type = tagteam_type
        tagteam.gender = gender
        tagteam.league_id = league_id
        tagteam.wrestler1_id = wrestler1_id
        tagteam.wrestler2_id = wrestler2_id
        tagteam.wrestler3_id = wrestler3_id if tagteam_type == 'trios' else None
        tagteam.manager = manager
        tagteam.finisher1 = finisher1
        tagteam.finisher2 = finisher2
        tagteam.finisher3 = finisher3
        tagteam.bio = bio
        tagteam.status = status

    db.session.commit()
    return tagteam
