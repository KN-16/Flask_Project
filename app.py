from flask import Flask,render_template
from config import Set_config
from flask_sqlalchemy import SQLAlchemy
app_=Flask(__name__)
try:
    Set_config(app_)
except:
    print("Error")
Db=SQLAlchemy(app_)

                      


