from flask_cors import CORS
from flask import Flask, jsonify, request

import json
import os
import pika
import sys
import time

from modules import icon
from modules import race_class

EXCHANGE = 'commands'

def make_app():
    app = Flask(__name__)
    CORS(app)

    @app.route('/generate')
    def status():
        return '{}\n\nicons: {}'.format(race_class.main(), icon.main(3))

    return app


if __name__ == '__main__':
    app = make_app()
    app.run(port=8000)
