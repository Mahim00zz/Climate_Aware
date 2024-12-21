from flask import Blueprint, jsonify, request
from datetime import datetime
import psycopg2
from psycopg2.extras import RealDictCursor
import os
from dotenv import load_dotenv

load_dotenv()


contributions = Blueprint("contributions", __name__)


def get_db_connection():
    try:
        conn = psycopg2.connect(
            dbname=os.getenv("DB_NAME", "climate_dashboard"),
            user=os.getenv("DB_USER", "your_db_user"),
            password=os.getenv("DB_PASSWORD", "your_db_password"),
            host=os.getenv("DB_HOST", "localhost")
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
                # Ensure the database table is available
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

        if not contributions:
            return jsonify({"message": "No contributions found"}), 200
        
        return jsonify(contributions), 200
    except Exception as e:
        return jsonify({"error": "Failed to fetch contributions", "details": str(e)}), 500
