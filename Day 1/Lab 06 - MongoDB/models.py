#!/usr/bin/env python3

#########################################################
# This is the database processing file. (aka. Models)
# It contains the DB connections, queries and processes.
# Uses principles of Models, Views, Controllers (MVC).
#########################################################

# Import modules required for app
import os
from pymongo import MongoClient
from werkzeug.utils import secure_filename

### Applicaiton configuration settings ###
# Set the database target to your local MongoDB instance
client = MongoClient('127.0.0.1:27017')
DB_NAME = "mongodb"  # This will be the name of your database
COL_NAME = "photos"  # This will be the name of your collection


##### Main body code #####

db = client[DB_NAME] # Create the database using the name provided and client connection to the MongoDB server
db_collection = db[COL_NAME]   # Create the collection using the name provided and database connection

# Retrieve all photos records from database
def get_photos():
    return db_collection.find({})

# Insert form fields into database
def insert_photo(request):
    title = request.form['title']
    comments = request.form['comments']
    filename = secure_filename(request.files['photo'].filename)
    thumbfile = filename.rsplit(".",1)[0] + "-thumb.jpg"

    db_collection.insert_one({'title':title, 'comments':comments, 'photo':filename, 'thumb':thumbfile})
