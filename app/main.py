from flask_cors import CORS
from flask import Flask, jsonify, request

import json

from modules import icon
from modules import race_class
from modules import background

EXCHANGE = 'commands'

def make_app():
    app = Flask(__name__)
    CORS(app)

    @app.route('/')
    @app.route('/generate')
    def status():
        character = race_class.main()
        character["icons"] = icon.main()
        character["background(s)"] = background.main()
        return json.dumps(character)

    return app


if __name__ == '__main__':
    app = make_app()
    app.run(port=8000)
