from flask_app import app
from flask import render_template,redirect,request
from flask_app.models.ninja import Ninja
from flask_app.models.dojo import Dojo

@app.route('/ninja_form', methods=["POST"])
def stick_in_ninja():
    data = {
        'fname' : request.form['fname'],
        'lname' : request.form['lname'],
        'age' : request.form['age'],
        'dojoid' : request.form['dojoid']
    }
    dojoid = request.form['dojoid']
    Ninja.new_ninja(data)
    return redirect(f'/show_dojo/{dojoid}')