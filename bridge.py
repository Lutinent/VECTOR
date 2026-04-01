from flask import Flask, request, jsonify
from flask_cors import CORS
import requests

app = Flask(__name__)
CORS(app) # Yeh line CORS error ko khatam kar degi

@app.route('/proxy', methods=['POST'])
def proxy():
    url = "https://integrate.api.nvidia.com/v1/chat/completions"
    headers = request.headers
    # NVIDIA ko request bhej raha hai
    response = requests.post(url, headers=dict(headers), json=request.json)
    return (response.content, response.status_code, response.headers.items())

if __name__ == '__main__':
    print("VICTOR Bridge is running on http://127.0.0.1:5000/proxy")
    app.run(port=5000)