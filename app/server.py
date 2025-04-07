from flask import Flask, redirect, request, jsonify, render_template 

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/submit', methods=['POST'])
def submit():
    inputURL = request.form.get('inputURL')  # Extract the form data
    if inputURL:
        # Process the input URL as needed
        
        return f"Data received: {inputURL}"
    else:
        return "No data received", 400

@app.route('/hello', methods=['GET'])
def hello():
    return jsonify({"message": "Hello, World!"})

@app.route('/<path:subpath>', methods=['GET'])
def handle_all_routes(subpath):

    # Process the subpath and redirect to the appropriate URL
    return redirect("https://www.google.co.in/")