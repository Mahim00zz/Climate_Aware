from flask import Blueprint, jsonify

resources = Blueprint("resources", __name__)

@resources.route('/resources', methods=['GET'])
def fetch_resources():
    resources_list = [
        {
            "title": "10 Ways to Reduce Your Carbon Footprint",
            "link": "https://www.austintexas.gov/blog/top-10-ways-reduce-your-carbon-footprint-and-save-money",
            "description": "Learn practical steps you can take every day to lower your environmental impact."
        },
        {
            "title": "Understanding Climate Change",
            "link": "https://www.un.org/en/climatechange/what-is-climate-change",
            "description": "A beginner-friendly guide to the science of climate change."
        },
    ]
    return jsonify(resources_list)
