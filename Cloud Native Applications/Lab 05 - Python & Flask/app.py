#!/usr/bin/env python3

##################################################
# This is the main application file.
# It has been kept to a minimum using the design
# principles of Models, Views, Controllers (MVC).
##################################################

# Import modules required for app
from flask import Flask, render_template, request

# Create a Flask instance
app = Flask(__name__)

##### Define routes #####
@app.route('/')
def home():
    return render_template('default.html',url="home")

##### Run the Flask instance, browse to http://localhost:5000 #####
if __name__ == "__main__":
	app.run(debug=False, host='localhost', port='5000', threaded=True)
