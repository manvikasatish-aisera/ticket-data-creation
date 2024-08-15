# Use an existing image as a base
# FROM node:14
FROM python:3.11.3

# Set the working directory
WORKDIR /usr/src/app

# Copy the rest of the code
COPY . .

RUN pip install --no-cache-dir -r requirements.txt

RUN ls -la

# set environment variables
ENV NUM_TICKETS numtickets
ENV DOMAIN domain

RUN mkdir -p /logs
RUN pwd
RUN ls /
WORKDIR src
CMD ["python3", "createticket.py"]
