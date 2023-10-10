# Set the base image as python:3.11
FROM python:3.11

# Update the package lists and install python3 and python3-pip
RUN apt-get update
RUN apt-get install -y python3 python3-pip

# Set the working directory inside the container as /app/
WORKDIR /app/

# Copy the contents of the current directory to the /app/ directory inside the container
COPY . /app/

# Install the Python dependencies specified in requirements.txt
RUN pip3 install -r requirements.txt

# Starting bot using python3
CMD ["python3", "/app/bot/main.py"]
