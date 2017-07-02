#!/usr/bin/python
# program principal 
from app import app
app = Flask(__name__)
app.run(debug=True)
