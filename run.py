from app import app_,Db
from models import Book
from route import Set_route
Set_route(app_)
with app_.app_context():
    Db.create_all()
if  __name__=="__main__":
    app_.run(debug=True)
