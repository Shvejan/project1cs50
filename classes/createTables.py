from booksusers import *
from flask import Flask,session
import os
import csv

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = os.getenv('DATABASE_URL2')
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
db.init_app(app)

def main():
    db.create_all()




if __name__ == '__main__':
    with app.app_context():
        main()
