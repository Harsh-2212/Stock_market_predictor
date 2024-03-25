from flask import Blueprint,render_template, request, flash, redirect, url_for
from .model import User, Note
from werkzeug.security import check_password_hash, generate_password_hash
from . import db

auth = Blueprint('auth',__name__)

@auth.route('/', methods=['GET','POST'])
def login():
    if request.method == 'POST':
        password = request.form.get('password')
        username = request.form.get('username')
        
        user = User.query.filter_by(username=username).first()
        
        if user:
            if check_password_hash(user.password, password):
                flash("Logged in Successfully!","success")
                return redirect(url_for("views.mainpage"))
            else:
                flash("Incorrect password!","error")
        else:
            flash("Email does not exist","error")
    return render_template('login.html')

@auth.route('/sign-up', methods=['GET','POST'])
def sign_up():
    if request.method == 'POST':
        email = request.form.get('email')
        password = request.form.get('password')
        username = request.form.get('username')

        user = User.query.filter_by(email=email).first()

        if user:
            flash("User already exists",'error')
            
        elif len(email) < 4:
            flash("Email should be greater than 4 characters","error")
        elif len(password) < 2:
            flash("Password should be greater than 2 characters","error")
        else: 
            new_user = User(email=email, username=username, password=generate_password_hash(password))
            db.session.add(new_user)
            db.session.commit()
            flash('Account Created!','success')
            return redirect(url_for("auth.login"))
        
    return render_template('sign_up.html')