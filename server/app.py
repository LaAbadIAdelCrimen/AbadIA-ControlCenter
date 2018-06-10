from flask import Flask, jsonify
from flask_cors import CORS
import os
import json

# configuration
DEBUG = True

# instantiate the app
app = Flask(__name__)
app.config.from_object(__name__)

# enable CORS
CORS(app)


# sanity check route
@app.route('/ping', methods=['GET'])
def ping_pong():
    return jsonify('pong!')

@app.route('/game', methods=['GET'])
def game():
    # filename = os.path.join("/tmp", "game.json"),
    with open("/tmp/game.json") as gamefile:
        data = json.load(gamefile)
    # abadia_actions_180608_235540_290496.json
    return jsonify({
        'status': 'success',
        'game': data
    })




if __name__ == '__main__':
    app.run()
