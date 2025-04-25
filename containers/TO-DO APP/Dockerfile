# Use Python 3.10 alpine version as a starting point
FROM docker.io/library/python:3.10-alpine

# Set our working directory inside the container to /app
WORKDIR /app

# Install system dependencies required for building Python packages
RUN apk add --no-cache gcc musl-dev libffi-dev

# Copy the list of required Python packages from our project to the container
COPY requirements.txt ./

# Install all the Python packages listed in requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

# Create the log directory and set permissions
RUN mkdir -p /var/log/flask-app && chmod -R 777 /var/log/flask-app

# Copy all of our project's files into the /app directory in the container
COPY . .

# Expose port 5000 to allow external connections
EXPOSE 5000

# Define the default command to run when the container starts
CMD ["flask", "run", "--host=0.0.0.0", "--port=5000"]