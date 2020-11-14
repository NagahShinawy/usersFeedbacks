from flask import Flask, render_template, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy

# flask app
app = Flask(__name__)
ENV = 'dev'


if ENV == 'dev':   # development

    DEBUG = True

    # The database URI that should be used for the connection.
    app.config["SQLALCHEMY_DATABASE_URI"] = 'postgresql://postgres:root@localhost/lexus'


else:   # production
    DEBUG = False
    app.config["SQLALCHEMY_DATABASE_URI"] = ''


# That's is because This requires extra memory and should be disabled if not needed.
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# db config
db = SQLAlchemy(app)