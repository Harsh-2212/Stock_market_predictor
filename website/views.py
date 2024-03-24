from flask import Blueprint,render_template

views = Blueprint('views',__name__)

@views.route('/')
def mainpage():
    return render_template("mainpage.html")