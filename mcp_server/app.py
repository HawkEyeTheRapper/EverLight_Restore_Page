import os
import json
from flask import Flask, jsonify, abort, send_from_directory

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
GISTS_INDEX = os.path.join(BASE_DIR, '..', 'gists_index.json')
GISTS_DIR = os.path.join(BASE_DIR, '..', 'gists')

app = Flask(__name__)

@app.route('/')
def home():
    return 'MCP server running'

@app.route('/gists')
def list_gists():
    try:
        with open(GISTS_INDEX, 'r', encoding='utf-8') as f:
            index = json.load(f)
        return jsonify(index)
    except FileNotFoundError:
        abort(404)

@app.route('/gists/<path:filename>')
def get_gist(filename):
    safe_path = os.path.normpath(filename)
    gist_path = os.path.join(GISTS_DIR, safe_path)
    if not os.path.isfile(gist_path) or not gist_path.startswith(os.path.abspath(GISTS_DIR)):
        abort(404)
    return send_from_directory(GISTS_DIR, safe_path)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8000)
