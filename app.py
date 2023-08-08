from flask import Flask,render_template
from config import Set_config
from flask_sqlalchemy import SQLAlchemy
app_=Flask(__name__)
Set_config(app_)
Db=SQLAlchemy(app_)

                      


