from flask import render_template,redirect,session,request, flash
from flask_app import app
from flask_app.models.tv_show import Tv_show
from flask_app.models.user import User


@app.route('/new/tv_show')
def new_tv_show():
    if 'user_id' not in session:
        return redirect('/logout')
    data = {
        "id":session['user_id']
    }
    return render_template('new_tv_show.html',user=User.get_by_id(data))


@app.route('/create/tv_show',methods=['POST'])
def create_tv_show():
    if 'user_id' not in session:
        return redirect('/logout')
    if not Tv_show.validate_tv_show(request.form):
        return redirect('/new/tv_show')
    data = {
        "name": request.form["name"],
        "description": request.form["description"],
        "instructions": request.form["instructions"],
        "under30": int(request.form["under30"]),
        "date_made": request.form["date_made"],
        "user_id": session["user_id"]
    }
    Tv_show.save(data)
    return redirect('/dashboard')

@app.route('/edit/tv_show/<int:id>')
def edit_tv_show(id):
    if 'user_id' not in session:
        return redirect('/logout')
    data = {
        "id":id
    }
    user_data = {
        "id":session['user_id']
    }
    return render_template("edit_tv_show.html",edit=Tv_show.get_one(data),user=User.get_by_id(user_data))

@app.route('/update/tv_show',methods=['POST'])
def update_tv_show():
    if 'user_id' not in session:
        return redirect('/logout')
    if not Tv_show.validate_tv_show(request.form):
        return redirect('/new/tv_show')
    data = {
        "name": request.form["name"],
        "description": request.form["description"],
        "instructions": request.form["instructions"],
        "under30": int(request.form["under30"]),
        "date_made": request.form["date_made"],
        "id": request.form['id']
    }
    Tv_show.update(data)
    return redirect('/dashboard')

@app.route('/tv_show/<int:id>')
def show_tv_show(id):
    if 'user_id' not in session:
        return redirect('/logout')
    data = {
        "id":id
    }
    user_data = {
        "id":session['user_id']
    }
    return render_template("show_tv_show.html",tv_show=Tv_show.get_one(data),user=User.get_by_id(user_data))

@app.route('/destroy/tv_show/<int:id>')
def destroy_tv_show(id):
    if 'user_id' not in session:
        return redirect('/logout')
    data = {
        "id":id
    }
    Tv_show.destroy(data)
    return redirect('/dashboard')