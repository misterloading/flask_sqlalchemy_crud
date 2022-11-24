from flask import Flask
from routes.contacts import contacts
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

# settings
app.secret_key = 'mysecret'
app.config["SQLALCHEMY_DATABASE_URI"] = f'mysql://noroot:noroot@localhost/test'
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

# no cache
app.config['SEND_FILE_MAX_AGE_DEFAULT'] = 0

SQLAlchemy(app)

app.register_blueprint(contacts)
