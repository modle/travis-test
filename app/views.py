from flask import render_template
from app import app

import json

from modules import icon
from modules import race_class
from modules import background

@app.route('/generate/raw')
def generate():
    character = race_class.main()
    character["icons"] = icon.main()
    character["backgrounds"] = background.main()
    return json.dumps(character)

@app.route('/')
@app.route('/generate')
def character():
    generated_char = generate()
    return render_template('index.html',
                           data=json.loads(generated_char),
                           as_json=generated_char
    )
