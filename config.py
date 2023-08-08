Server_name="LAPTOP-C6VJ3RCH\SQLEXPRESS"
Db_name="KN16"
Db_driver="ODBC+Driver+17+for+SQL+Server"
SQLALCHEMY_DATABASE_URI=f"mssql+pyodbc://{Server_name}/{Db_name}?driver={Db_driver}"
def Set_config(app):
    app.config["SQLALCHEMY_DATABASE_URI"]=SQLALCHEMY_DATABASE_URI
    app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False