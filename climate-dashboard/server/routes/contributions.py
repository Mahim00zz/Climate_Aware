from flask import Blueprint, jsonify, request
from datetime import datetime
import psycopg2
from psycopg2.extras import RealDictCursor

contributions = Blueprint("contributions", __name__)

# Database connection
def get_db_connection():
    try:
        conn = psycopg2.connect(
            dbname="climate_dashboard",
            user="your_db_user",
            password="your_db_password",
            host="localhost"
        )
        return conn
    except Exception as e:
        raise ConnectionError(f"Failed to connect to the database: {e}")

@contributions.route('/contributions', methods=['POST'])
def add_contribution():
    data = request.json
    user_name = data.get("user_name", "Anonymous")
    tip = data.get("tip")

    if not tip:
        return jsonify({"error": "Tip cannot be empty"}), 400

    try:
        with get_db_connection() as conn:
            with conn.cursor() as cur:
                cur.execute(
                    "INSERT INTO user_contributions (user_name, tip, timestamp) VALUES (%s, %s, %s)",
                    (user_name, tip, datetime.now())
                )
                conn.commit()
        return jsonify({"message": "Contribution added successfully!"}), 201
    except Exception as e:
        return jsonify({"error": "Failed to add contribution", "details": str(e)}), 500

@contributions.route('/contributions', methods=['GET'])
def get_contributions():
    try:
        with get_db_connection() as conn:
            with conn.cursor(cursor_factory=RealDictCursor) as cur:
                cur.execute("SELECT user_name, tip, timestamp FROM user_contributions")
                contributions = cur.fetchall()
        return jsonify(contributions), 200
    except Exception as e:
        return jsonify({"error": "Failed to fetch contributions", "details": str(e)}), 500