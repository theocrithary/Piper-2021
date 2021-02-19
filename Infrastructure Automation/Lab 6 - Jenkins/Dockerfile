# Use an official Python container as a parent image
FROM --platform=linux/386 python:latest

# Set the working directory to /usr/src/app
WORKDIR /usr/src/app

# Copy the current directory contents into the container
COPY . ./

# Install any needed packages specified in requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

# Make port 5000 available to the world outside this container
EXPOSE 80

# Run app.py when the container launches
CMD ["python", "app.py"]
