from flask import Flask, jsonify
import requests

app = Flask(__name__)

@app.route('/statuses', methods=['GET'])
def get_statuses():
    api_url = 'https://api.example.com/statuses' 
    headers = {'Authorization': 'Bearer <your_access_token>'}

    response = requests.get(api_url, headers=headers)

    if response.status_code == 200:
        statuses = response.json()
        return jsonify(statuses), 200
    else:
        return jsonify({'error': 'Failed to fetch statuses'}), response.status_code

if __name__ == '__main__':
    app.run()