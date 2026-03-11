#!/usr/bin/python3

import sys
import os

# Add your project directory to sys.path
project_home = '/home/VECTOR000/highrise_bot'
if project_home not in sys.path:
    sys.path = [project_home] + sys.path

# Set working directory
os.chdir(project_home)

# Import your Flask app (must be named "application")
from flask_app import app as application

# For debugging, you can add this section
if __name__ == '__main__':
    application.run(debug=True)