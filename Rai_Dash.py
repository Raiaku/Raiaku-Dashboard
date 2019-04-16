
#in the terminal read documentation for debug ability on flask site
#to run normally `set -x FLASK_APP Rai_Dash.py; flask run`

from datetime import datetime
from flask import Flask, render_template, url_for, flash, redirect
from flask_sqlalchemy import SQLAlchemy
from forms import RegistrationForm, LoginForm

app = Flask(__name__)
app.config['SECRET_KEY'] = '6d819c27c08921040d09e98b13ec0a56'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///site.db'
db = SQLAlchemy(app)

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(20), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    image_file = db.Column(db.String(20), nullable=False, default='default.jpg')
    password = db.Column(db.String(60), nullable=False)
    post = db.relationship('Post', backref='author' lazy=True)

    def __repr__(self):
        return f"User('{self.username}', '{self.email}', '{self.image_file}')"


class Post(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable=False)
    date_posted = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
    content = db.Column(db.text, nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)

    def __repr__(self):
        return f"Post('{self.title}', '{self.date_posted}')"

# dummy data for testing
# not the dummy
post = [
    {
        'author': 'Genure Smith',
        'title': 'Blog Post 1',
        'content': 'First post content',
        'date_posted': 'April 9, 2019'
    },
    {
        'author': 'Raiaku Pyrogale',
        'title': 'Blog Post 2',
        'content': 'Second post content',
        'date_posted': 'April 10, 2019'
    }
]

@app.route("/")
def hello():
    return render_template('hello.html', title='Hello')


@app.route("/home")
def home():
    return render_template('home.html', post=post)


@app.route("/about")
def about():
    return render_template('about.html', title='About')

#future proofing for API's/Apps that i may want to add later 
@app.route("/spotify")
def spotify():
    return "<h1>Spotify Page</h1>"
    #return render_template('')

@app.route("/manga")
def manga():
    return "<h1>Manga Page</h1>"
    #return render_template('')

@app.route("/gmail")
def gmail():
    return "<h1>Gmail Page</h1>"
    #return render_template('')

@app.route("/kickstarter")
def kickstarter():
    return "<h1>Kickstarter Suggestion Page</h1>"
    #return render_template('')

@app.route("/register", methods=['GET', 'POST'])
def register():
    form = RegistrationForm()
    if form.validate_on_submit():
        flash(f'Account created for {form.username.data}!', 'success')
        return redirect(url_for('home'))
    return render_template('register.html', title='Register', form=form)

@app.route("/login", methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        #below is dummy data for testing 
        if form.email.data == 'admin@blog.com' and form.password.data == 'password':
            flash('You have been logged in!', 'success')
            return redirect(url_for('home'))
        else:
            flash('Login Unsuccessful. Please check username and password', 'danger')
        #end of dummy data
    return render_template('login.html', title='Login', form=form)


#this is for when/if i want to run the python application directly
#this way i can make changes with out having to restart the web server
if __name__ == '__main__':
    app.run(debug=True)