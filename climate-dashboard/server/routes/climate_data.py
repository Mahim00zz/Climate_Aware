from flask import Blueprint, jsonify, request
import os
import requests

climate_data = Blueprint("climate_data", __name__)

@climate_data.route('/climate-data', methods=['GET'])
def fetch_climate_data():
   
    api_url = "https://api.openweathermap.org/data/2.5/weather"
    
    
    api_key = os.getenv("OPENWEATHERMAP_API_KEY", "your_default_api_key")
    if not api_key or api_key == "your_default_api_key":
        return jsonify({"error": "API key is missing or not set"}), 500
    

    lat = request.args.get("lat", "40.7128")  
    lon = request.args.get("lon", "-74.0060")  

    params = {
        "lat": lat,
        "lon": lon,
        "appid": api_key,
        "units": "metric",  
    }

    
    try:
        response = requests.get(api_url, params=params)
        response.raise_for_status()
    except requests.exceptions.RequestException as e:
        return jsonify({"error": "Failed to fetch data", "details": str(e)}), 500

    
    return jsonify(response.json())
