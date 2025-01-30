from flask import Flask, jsonify
from flask_cors import CORS
from datetime import datetime

app = Flask(__name__)
CORS(app)  # Enable CORS for all routes

@app.route('/', methods=['GET'])
def get_info():
    # Define the required data
    data = {
        "email": "akinolaakinkunmifa@gmail.com",
        "current_datetime": datetime.utcnow().isoformat() + "Z", 
        "github_url": "https://github.com/yourusername/your-repo" 
    }
    return jsonify(data), 200 

if __name__ == '__main__':
    app.run(debug=True)  # Run the app in debug mode