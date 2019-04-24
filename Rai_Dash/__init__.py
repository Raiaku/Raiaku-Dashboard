
# the following line was commented out as i moved it to the models.py file along with the User and Post modules made earlier 
# from datetime import datetime
from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
# to make secret key:
# opened and interactive ide (ipython) and did `import secrets`
#followed by `secrets.tocken_hex(16)` for a 16 digit random key 
app.config['SECRET_KEY'] = '6d819c27c08921040d09e98b13ec0a56'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///site.db'
db = SQLAlchemy(app)

from Rai_Dash import routes