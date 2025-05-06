# app.py (or any other Python file you're using)

from flask import Flask, jsonify

app = Flask(__name__)

# A simple API route to test
@app.route('/test', methods=['GET'])
def test_api():
    return jsonify({"message": "Keploy test successful!"})

if __name__ == '__main__':
    app.run(debug=True)
