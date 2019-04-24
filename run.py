
# in the terminal read documentation for debug ability on flask site
# to run normally `set -x FLASK_APP Rai_Dash.py; flask run`

from Rai_Dash import app

#this is for when/if i want to run the python application directly
#this way i can make changes with out having to restart the web server
if __name__ == '__main__':
    app.run(debug=True)