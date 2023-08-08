from flask import render_template,request,redirect,jsonify
from models import get_id_book,get_all_book_ListType,update_quantity_of_bookid,dellete_book_db_id,Book
def Set_route(app):
    @app.route("/")
    def Home_page():
        return render_template("Home_Page.html")
    @app.route("/get_book_id")
    def Get_book_id():
                rq_data=request.get_json(silent=True)
                if rq_data!=None:
                    try:
                        id=rq_data["ID"]
                    except KeyError:
                        return "Missing key \"ID\" "
                    if get_id_book(id)!=None:
                        return jsonify(get_id_book(id))
                    else: return f"Error get ID: {id} of DatabaseBook"
                else:return "Please send Request Header-Content type: application/json"    
    @app.route("/get_all_book")
    def Get_all_book():
         return jsonify({"All Book":get_all_book_ListType()})
    @app.route("/update_book_id",methods=["PUT"])
    def Update_book():
        rq_data=request.get_json(silent=True)
        if rq_data!=None:
            try:
                id=rq_data["ID"]
            except KeyError:
                 return "Missing key \"ID\" "
            try:
                quantity=rq_data["QUANTITY"]
            except KeyError:
                quantity=0    
            if update_quantity_of_bookid(id,quantity):
                return "Update Success"
            else:return f"Update Error,Maybe ID: {id} or Quantity: {quantity} is not valid"
        else:return "Please send Request Header-Content type: application/json"     
    @app.route("/delete_book",methods=["DELETE"])
    def Delete_book_id():
        rq_data=request.get_json(silent=True)
        if rq_data!=None:
            try:
                id=rq_data["ID"]
            except KeyError:
                return "Missing key \"ID\" " 
            return dellete_book_db_id(id)        
        else:return "Please send Request Header-Content type: application/json" 
    @app.route("/add_book",methods=["POST"])
    def Add_book():
        rq_data=request.get_json(silent=True)
        if rq_data!=None:
            try:
                id=rq_data["ID"]
            except KeyError:
                 return "Missing key \"ID\" "
            try:
                quantity=rq_data["QUANTITY"]
            except KeyError:
                quantity=0 
            try:
                name=rq_data["NAME"]
            except KeyError:
                name="Please, Update Name"  
            try:
                price=rq_data["PRICE"]
            except:
                price=0     
            Book_new=Book(id,quantity,name,price)
            return Book_new.add_book_db()
        else:return "Please send Request Header-Content type: application/json"
