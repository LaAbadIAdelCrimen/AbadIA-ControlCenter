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

# AbadIA

loadedGame    = {}
loadedActions = []

# sanity check route
@app.route('/ping', methods=['GET'])
def ping_pong():
    return jsonify('pong!')

@app.route('/game', methods=['GET'])
def game():
    # filename = os.path.join("/tmp", "game.json"),
    actions = []
    with open("/tmp/game.json") as gameFile:
            for cnt, line in enumerate(gameFile):
                # print("Line {}: {}".format(cnt, line))
                actions.append(json.loads(line)[0])
    loadedActions = actions
    loadedGame.update({'filename': '/tmp/game.json', 'actions': len(actions)})

    # abadia_actions_180608_235540_290496.json
    return jsonify({
        'status': 'success',
        'game': loadedGame
    })

@app.route('/action/<index>', methods=['GET'])
def action(index):
    print("index ({})".format(index))
    print("game ({})".format(loadedGame))
    print("actions ({})".format(loadedActions))
    # print("action {}".format(loadedActions[int(index)]))
    if len(loadedActions) > int(index):
        action = loadedActions[int(index)]
    else:
        action = []

    return jsonify({
        'status': 'success',
        'game': game,
        'action': action
    })



if __name__ == '__main__':
    app.run()
