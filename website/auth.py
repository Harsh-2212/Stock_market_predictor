from flask import Blueprint,render_template, request, flash, redirect, url_for
from .model import User, Note
from werkzeug.security import check_password_hash, generate_password_hash
from . import db

auth = Blueprint('auth',__name__)

@auth.route('/login', methods=['GET','POST'])
def login():
    return render_template('login.html')

@auth.route('/sign-up', methods=['GET','POST'])
def sign_up():
    # if request.method == 'POST':
    #     email = request.form.get('email')
    #     password = request.form.get('password')
    #     username = request.form.get('username')

    #     user = User.query.filter_by(email=email).first()

    #     if user:
    #         flash("User already exists",'error')
            
    #     elif len(email) < 4:
    #         flash("Email should be greater than 4 characters","error")
    #     elif len(password) < 2:
    #         flash("Password should be greater than 2 characters","error")
    #     else: 
    #         new_user = User(email=email, username=username, password=generate_password_hash(password, method='sha256'))
    #         db.session.add(new_user)
    #         db.session.commit()
    #         flash('Account Created!','success')
    #         return redirect(url_for("auth.login"))
    data = request.form
    print(data)
        
    return render_template('sign_up.html')