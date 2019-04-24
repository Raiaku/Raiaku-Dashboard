
from flask import render_template, url_for, flash, redirect
from Rai_Dash import app
from Rai_Dash.forms import RegistrationForm, LoginForm
from Rai_Dash.models import User, Post


# dummy data for testing
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
