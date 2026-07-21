from flask import Flask, render_template, request, redirect, url_for, session
from flask_sqlalchemy import SQLAlchemy
from werkzeug.security import generate_password_hash, check_password_hash
import numpy as np
import pickle

app = Flask(__name__)
app.secret_key = "movie_secret_key"

# ================= DATABASE CONFIG =================
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///users.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

# ================= USER MODEL =================
class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(100), unique=True, nullable=False)
    password = db.Column(db.String(200), nullable=False)

# ================= LOAD MODEL =================
model = pickle.load(open('model.pkl', 'rb'))

# ================= LOAD ENCODERS =================
le_title = pickle.load(open('title.pkl', 'rb'))
le_genre = pickle.load(open('genre.pkl', 'rb'))
le_director = pickle.load(open('director.pkl', 'rb'))
le_actor = pickle.load(open('lead_actor.pkl', 'rb'))
le_country = pickle.load(open('country.pkl', 'rb'))

titles = le_title.classes_
genres = le_genre.classes_
directors = le_director.classes_
actors = le_actor.classes_
countries = le_country.classes_

# ================= CREATE DB =================
with app.app_context():
    db.create_all()

# ================= ROUTES =================

@app.route('/')
def home():
    return render_template('home.html')


# -------- REGISTER --------
@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']

        if User.query.filter_by(username=username).first():
            return render_template('register.html', error="Username already exists")

        hashed_pw = generate_password_hash(password)
        new_user = User(username=username, password=hashed_pw)
        db.session.add(new_user)
        db.session.commit()

        return redirect(url_for('login'))

    return render_template('register.html')


# -------- LOGIN --------
@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']

        user = User.query.filter_by(username=username).first()

        if user and check_password_hash(user.password, password):
            session['user'] = user.username
            return redirect(url_for('predict'))

        return render_template('login.html', error="Invalid username or password")

    return render_template('login.html')


# -------- PREDICT --------
@app.route('/predict', methods=['GET', 'POST'])
def predict():
    if 'user' not in session:
        return redirect(url_for('login'))

    if request.method == 'POST':
        title = le_title.transform([request.form['title']])[0]
        genre = le_genre.transform([request.form['genre']])[0]
        director = le_director.transform([request.form['director']])[0]
        actor = le_actor.transform([request.form['actor']])[0]
        country = le_country.transform([request.form['country']])[0]

        features = np.array([[
            title,
            genre,
            int(request.form['year']),
            int(request.form['day']),
            country,
            float(request.form['budget']),
            float(request.form['us_box']),
            float(request.form['global_box']),
            float(request.form['opening']),
            float(request.form['imdb']),
            float(request.form['rt']),
            int(request.form['imdb_votes']),
            int(request.form['rt_votes']),
            director,
            actor,
            int(request.form['month'])
        ]])

        prediction = model.predict(features)[0]
        return render_template('result.html', result=round(prediction, 2))

    return render_template(
        'predict.html',
        titles=titles,
        genres=genres,
        directors=directors,
        actors=actors,
        countries=countries
    )


# -------- LOGOUT --------
@app.route('/logout')
def logout():
    session.clear()
    return redirect(url_for('home'))


if __name__ == '__main__':
    app.run(debug=True)
