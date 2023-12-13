from flask import Flask
app=Flask(__name__)
app.secret_key="project"
DATABASE="lili_3amty"

UPLOAD_FOLDER = "c:/Users/bouaz/OneDrive/Desktop/python_project/Aziz/flask_app/static/data_base_img"
ALLOWED_EXTENSIONS = {'txt', 'pdf', 'png', 'jpg', 'jpeg', 'gif'}