from flask import Flask, jsonify, request
from flask_cors import CORS
from urllib.parse import urlparse
from concurrent.futures import ThreadPoolExecutor
import requests
import logging

app = Flask(__name__)
CORS(app)

logging.basicConfig(level=logging.INFO)

@app.before_request
def log_request_info():
    app.logger.info(f"Incoming Request: {request.method} {request.url}")

@app.after_request
def log_response_info(response):
    app.logger.info(f"Response Status: {response.status_code}")
    return response

def is_valid_url(url):
    try:
        result = urlparse(url)
        return all([result.scheme, result.netloc])
    except:
        return False

def fetch_data(url):
    try:
        response = requests.get(url)
        if response.status_code == 200:
            data = response.json()
            return data.get("data", [])
        else:
            return []
    except:
        return []

@app.route("/notifications", methods=["GET"])
def notification_system():
    if request.headers.get("Authorization") == "Bearer <valid_token>":
        notifications = [
            {"id": 1, "message": "Notification 1"},
            {"id": 2, "message": "Notification 2"}
        ]
        print("Task 1 completed")
        return jsonify({"notifications": notifications})
    else:
        return jsonify({"message": "Please log in to view notifications"}), 401

@app.route("/vehicle_mc", methods=["GET"])
def vehicle_mc():
    urls = request.args.get('url')

    if not is_valid_url(urls):
        return jsonify({
            "error": "Invalid URL"
        })

    with ThreadPoolExecutor() as executor:
        future = executor.submit(fetch_data, urls)
        data = future.result()
    return jsonify({"data": data})

if __name__ == "__main__":
    app.run(debug=True)