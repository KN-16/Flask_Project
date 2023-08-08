import app
from sqlalchemy import Column, Integer, String,Float
#Crud,RestFull (JSON Value)
class Book(app.Db.Model):
    __tablename__="Book"
    ID=Column(Integer,primary_key=True,nullable=False)
    Name=Column(String(50),nullable=False)
    Quantity=Column(Integer,nullable=False)
    Price=Column(Float,nullable=False)
    Total=Column(Float,nullable=False)
    def json(self):
        return {"ID: ":self.ID,"Name: ":self.Name,"Quantity: ":self.Quantity,"Price: ":self.Price,"Total: ":self.Total}
        
    def __init__(self,id,quantity,name,price):
        self.ID=id
        self.Quantity=quantity
        self.Name=name
        self.Price=price
        self.Total=price*quantity
    #Create
    def add_book_db(self):
        if app.Db.session.query(Book).filter(Book.ID==self.ID).first()==None:
            app.Db.session.add(self)
            app.Db.session.commit()
            return "Add Success"
        else: return f"Add Error, May be ID: {self.ID} is not Valid"
    #READ
def get_all_book_ListType():
    return [tmp.json() for tmp in app.Db.session.query(Book).all()]
def get_id_book(id):
    tmp=app.Db.session.query(Book).filter(Book.ID==id).first()
    if tmp!=None:
        return tmp.json()
    return None 
    #Delete
def dellete_book_db_id(id):
        if app.Db.session.query(Book).filter(Book.ID==id).first()!=None:
            app.Db.session.query(Book).filter(Book.ID==id).delete()
            app.Db.session.commit()
            return "Delete Success"
        else:return f"Delete Error,Maybe ID is not valid(Database not have ID: {id}"   
    #Update
def update_quantity_of_bookid(id,quantity_new):
    tmp=app.Db.session.query(Book).filter(Book.ID==id).first() 
    if tmp!=None:
        tmp.Quantity=quantity_new
        tmp.Total=tmp.Quantity*tmp.Price
        app.Db.session.commit()
        return True
    return False   

    