
from flask import Blueprint, jsonify, request
import os
import requests

climate_data = Blueprint("climate_data", __name__)

@climate_data.route('/climate-data', methods=['GET'])
def fetch_climate_data():
    api_url = "https://api.openweathermap.org/data/2.5/weather"
    api_key = os.getenv("OPENWEATHERMAP_API_KEY")  

    if not api_key:
        return jsonify({"error": "API key is missing or not set"}), 500

    lat = request.args.get("lat", "40.7128")
    lon = request.args.get("lon", "-74.0060")

    try:
        lat = float(lat)
        lon = float(lon)
    except ValueError:
        return jsonify({"error": "Invalid latitude or longitude values"}), 400

    params = {
        "lat": lat,
        "lon": lon,
        "appid": api_key,
        "units": "imperial"  
    }

    # Making the API call
    try:
        response = requests.get(api_url, params=params)
        response.raise_for_status() 
    except requests.exceptions.RequestException as e:
        return jsonify({"error": "Failed to fetch data", "details": str(e)}), 500

    return jsonify(response.json())  
