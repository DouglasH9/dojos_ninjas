from flask_app import app
from flask import render_template,redirect,request
from flask_app.models.dojo import Dojo
from flask_app.models.ninja import Ninja

@app.route('/new_dojo')
def new_dojo():
    dojos = Dojo.get_all()
    return render_template('new_dojo.html', dojos = dojos)

@app.route('/create_dojo', methods=["POST"])
def add_new_dojo():
    data = {
        "nDojo" : request.form['nDojo']
    }
    Dojo.add_new_dojo(data)
    return redirect('/new_dojo')

@app.route('/show_dojo/<int:id>')
def show_dojo(id):
    data = {
        'id': id,
    }
    ninja_list = Dojo.show_dojo_ninjas(data)
    dojo_name = Dojo.show_dojo(data)
    return render_template('show_dojo.html', ninjas = ninja_list, name = dojo_name)

@app.route('/add_ninja')
def add_ninja():
    dlist = Dojo.get_all_dojos()
    return render_template('add_ninja.html', dlist = dlist)

@app.route('/delete_dojo/<int:id>', methods=['POST'])
def delete_dojo(id):
    data = {
        'id' : id
    }
    Dojo.delete_the_dojo(data)
    return redirect('/new_dojo')

