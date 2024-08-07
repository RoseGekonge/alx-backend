#!/usr/bin/env python3
"""
A Basic flask application
"""
from flask import Flask
from flask import render_template
from flask_babel import Babel


class Config(object):
    """
    Application configuration class for language and timezone
    """
    LANGUAGES = ['en', 'fr']
    BABEL_DEFAULT_LOCALE = 'en'
    BABEL_DEFAULT_TIMEZONE = 'UTC'


# Creating a new flask app
app = Flask(__name__)

# This is meant to apply the configaration to the flask app
app.config.from_object(Config)

# Instantiate the application object and storing it in a module-level variable named babel
babel = Babel(app)


@app.route('/', strict_slashes=False)
def index() -> str:
    """
    Renders a basic html template
    """
    return render_template('1-index.html')


if __name__ == '__main__':
    app.run()
