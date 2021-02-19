#!/usr/bin/env python3

##################################################
# This is the main application file.
# It has been kept to a minimum using the design
# principles of Models, Views, Controllers (MVC).
##################################################

# Import modules required for app
import os
from flask import Flask

# Create a Flask instance
app = Flask(__name__)

##### Define routes #####
@app.route("/")
def index():
    html = """<h3>Hello World!</h3><br>
            This is a basic web page written in Python and served by Flask
            """.format()
    return html

##### Run the Flask instance, browse to http://<< Host IP or URL >>:port #####
if __name__ == "__main__":
    app.run(host='0.0.0.0', port=7001)
