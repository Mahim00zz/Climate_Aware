from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from dotenv import load_dotenv
from datetime import datetime
import os

# Load .env.local from the root directory
load_dotenv(os.path.join(os.path.dirname(os.path.dirname(__file__)), '.env.local'))


app = Flask(__name__)

# Fetch DATABASE_URL from the environment
database_url = os.getenv("DATABASE_URL")
print("DATABASE_URL:", os.getenv("DATABASE_URL"))


if not database_url:
    raise RuntimeError("DATABASE_URL is not set in the environment variables.")

# Set up SQLAlchemy configuration
app.config['SQLALCHEMY_DATABASE_URI'] = database_url
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Initialize the database
db = SQLAlchemy(app)

class UserTip(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    content = db.Column(db.String(500))
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    
    def __repr__(self):
        return f'<UserTip {self.content}>'
