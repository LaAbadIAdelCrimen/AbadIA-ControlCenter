from typing import List, Any

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
loadedActions = {}

# sanity check route
@app.route('/ping', methods=['GET'])
def ping_pong():
    return jsonify('pong!')

@app.route('/game', methods=['GET'])
def game():
    # filename = os.path.join("/tmp", "game.json"),
    global loadedActions
    global loadedGame

    loadedActions = {}

    with open("/tmp/game.json") as gameFile:
            for cnt, line in enumerate(gameFile):
                # print("Line {}: {}".format(cnt, line))
                loadedActions.update({str(cnt): json.loads(line)[0]})
    # loadedActions = actions
    loadedGame.update({'filename': '/tmp/game.json', 'actions': len(loadedActions)})

    # abadia_actions_180608_235540_290496.json
    return jsonify({
        'status': 'success',
        'game': loadedGame
    })

@app.route('/action/<index>', methods=['GET'])
def action(index):
    global loadedActions
    global loadedGame

    print("index ({})".format(index))
    print("game ({})".format(loadedGame))
    print("actions ({})".format(loadedActions[index]))
    # print("action {}".format(loadedActions[int(index)]))

    if int(index) > len(loadedActions) or len(loadedActions) == 0:
        step = {'action': {}}
    else:
        step = loadedActions[index]

    if int(index)+1 == len(loadedActions):
        next = index
    else:
        next = str(int(index)+1)

    if int(index)-1 < 0:
        prev = '0'
    else:
        prev = str(int(index)-1)


    ddreji = []

    step['action']['reji'] = reji

    return jsonify({
        'status': 'success',
        'game': loadedGame,
        'next': next,
        'prev': prev,
        'action': step['action']

    })



if __name__ == '__main__':
    app.run()
