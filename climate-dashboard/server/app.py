from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from dotenv import load_dotenv
from datetime import datetime
import os
from routes.climate_data import climate_data 

# Load environment variables from .env.local file
load_dotenv(os.path.join(os.path.dirname(__file__), '.env.local'))

# Initialize Flask app
app = Flask(__name__)

app.register_blueprint(climate_data, url_prefix='/')  # Register with base URL as '/'

if __name__ == '__main__':
    app.run(debug=True)
    
# Fetch the DATABASE_URL from environment variables
database_url = os.getenv("DATABASE_URL")
if not database_url:
    raise RuntimeError("DATABASE_URL is not set in the environment variables.")

# Configure the SQLAlchemy database connection
app.config['SQLALCHEMY_DATABASE_URI'] = database_url
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False 

# Initialize SQLAlchemy
db = SQLAlchemy(app)

# Define UserTip model for storing climate tips
class UserTip(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    content = db.Column(db.String(500))  # Tip content (string length 500 max)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)  # Timestamp for when the tip was added

    def __repr__(self):
        return f'<UserTip {self.content}>'

# Route for the home page
@app.route('/')
def home():
    return """
    <h1>Welcome to the Climate Awareness Dashboard!</h1>
    <p>Use the following endpoints:</p>
    <ul>
        <li><b>POST /add_tip</b> to add a new climate tip</li>
        <li><b>GET /get_tips</b> to view all submitted tips</li>
    </ul>
    """

# Route to add a new climate tip
@app.route('/add_tip', methods=['POST'])
def add_tip():
    # Ensure the request is in JSON format
    if not request.is_json:
        return jsonify({"error": "Invalid input. JSON required."}), 400

    # Extract content from the request JSON
    content = request.json.get('content')

    if content:
        # Create a new UserTip instance and add it to the database
        tip = UserTip(content=content)
        db.session.add(tip)
        db.session.commit()  
        return jsonify({"message": "Tip added!"}), 201
    else:
        return jsonify({"error": "Content is missing!"}), 400

# Route to retrieve all climate tips
@app.route('/get_tips', methods=['GET'])
def get_tips():
    # Query all tips from the database
    tips = UserTip.query.all()

    # Return tips in JSON format
    return jsonify([{'id': tip.id, 'content': tip.content, 'created_at': tip.created_at} for tip in tips])

# Initialize the database and create tables if they don't exist
with app.app_context():
    db.create_all()  

# Run the app in debug mode
if __name__ == '__main__':
    app.run(debug=True)
