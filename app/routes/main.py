from flask import Blueprint, jsonify, render_template, redirect, request
from app.models.urls import URL
from app import db
from app.services.generate_key import generate_key
from app.config import Config

main_bp = Blueprint('main', __name__)

@main_bp.route("/")
def home():
    return render_template('home.html')

@main_bp.route('/submit', methods=['POST'])
def submit():
    inputURL = request.form.get('inputURL')  # Extract the form data
    if inputURL:
        # Generate a unique key for the URL and store it in db
        key = generate_key(inputURL)

        # Here you would typically save the URL to the database or perform some action
        return jsonify({"shortifiedURL":  Config.SERVER_NAME + "/" + key, "originalUrl": inputURL}), 200  # Return the generated key as JSON response
    else:
        return "No data received", 400

@main_bp.route('/hello', methods=['GET'])
def hello():
    return jsonify({"message": "Hello, World!"})

@main_bp.route('/<path:subpath>', methods=['GET'])
def handle_all_routes(subpath):

    # Check if the subpath exists in the database
    url_entry = URL.query.filter_by(id=subpath).first()
    if url_entry:
        # If it exists, redirect to the original URL
        original_url = url_entry.url
        return redirect(original_url, code=302)
    else:
        # If it doesn't exist, return a 404 error or handle it as needed
        return jsonify({"error": "URL not found"})
