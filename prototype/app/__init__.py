from flask import Flask

# Config Values
UPLOAD_FOLDER = './app/static/uploads/'
USERNAME = 'travel'
PASSWORD = 'OMNI-dev'

# SECRET_KEY is needed for session security, the flash() method in this case stores the message in a session
SECRET_KEY = 'Sup3r$3cretkey'

app = Flask(__name__)
app.config.from_object(__name__)
from app import views
