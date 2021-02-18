#!/usr/bin/env python3

##################################################
# This is the main application file.
# It has been kept to a minimum using the design
# principles of Models, Views, Controllers (MVC).
##################################################

# Import modules required for app
from flask import Flask, render_template, request
from models import get_photos, insert_photo, upload_photo

# Create a Flask instance
app = Flask(__name__)

##### Define routes #####
@app.route('/')
def home():
    album_photos = get_photos()							# Call function in 'models.py' to retrieve all photo's from database
    return render_template('default.html',album_photos=album_photos,url="home")

# This route accepts GET and POST calls
@app.route('/upload', methods=['POST'])
def upload():
	insert_photo(request)								# Call function in 'models.py' to process the database transaction
	upload_photo(request.files['photo'])				# Call function in 'models.py' to upload photo to ECS
	return render_template('submit-photo.html')			# Return a page to inform the user of a successful upload

@app.route('/photo/<path:photo>')
def photo(photo):
    return render_template('photo.html',photo=photo)

##### Run the Flask instance, browse to http://localhost:5000 #####
if __name__ == "__main__":
	app.run(debug=False, host='localhost', port='5000', threaded=True)
