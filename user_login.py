from flask import Flask, render_template, url_for, request, redirect, flash
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__, template_folder="templates")
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///login.sqlite3'
app.secret_key = 'super secret key'
db = SQLAlchemy(app)


class User(db.Model):
    id = db.Column('user_id', db.Integer, primary_key=True)
    name = db.Column(db.String(100))
    password = db.Column(db.String(50))


@app.route('/', methods=['GET', 'POST'])
def test():
    if request.method == 'POST':
        username = request.form['name']
        password = request.form['pwd']
        print(username, password)
        user = User(name=username, password=password)
        db.session.add(user)
        db.session.commit()
        # flash('Record was successfully added')
        return redirect(url_for('get_users'))
    return render_template('hello.html')


@app.route('/user')
def get_users():
    data = User.query.all()
    return render_template('listusers.html', data=data)


@app.route('/delete/<int:id>')
def delete(id):
    User.query.filter(User.id == id).delete()
    db.session.commit()
    return redirect(url_for('get_users'))


app.run(debug=True)
