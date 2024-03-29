from flask import Blueprint, render_template, request, flash, jsonify
from flask_login import login_required, current_user
from .models import Post
from . import db
import json
# import folium

views = Blueprint('views', __name__)


@views.route('/')
def index():
    #return "<h1>Test</h1>"
    return render_template("index.html", user=current_user)


@views.route('/home', methods=['GET', 'POST'])
#@login_required
def home():
    if request.method == 'POST': 
        post = request.form.get('post') # Gets the post from the HTML 

        if len(post) < 1:
            flash('Post is too short!', category='error') 
        else:
            new_post = Post(data=post, user_id=current_user.id)  #providing the schema for the post 
            db.session.add(new_post) #adding the post to the database 
            db.session.commit()
            flash('Post added!', category='success')
    
    #return "<p>home</p>"
    return render_template("home.html", user=current_user)


@views.route('/home/map') # methods=['GET', 'POST']
@login_required
def map():
    return render_template("map.html", user=current_user)


@views.route('/delete-post', methods=['POST'])
def delete_post():  
    post = json.loads(request.data) # this function expects a JSON from the INDEX.js file 
    postId = post['postId']
    post = Post.query.get(postId)
    if post:
        if post.user_id == current_user.id:
            db.session.delete(post)
            db.session.commit()

    return jsonify({})

  