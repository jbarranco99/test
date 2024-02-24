from flask import Flask, jsonify, request
import os

app = Flask(__name__)


@app.route('/', methods=['POST'])
def index():
    pickedCats = req_data['pickedCats']
    return jsonify("pickedCats":pickedCats)


if __name__ == '__main__':
    app.run(debug=True, port=os.getenv("PORT", default=5000))
