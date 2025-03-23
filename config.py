Server_name="LAPTOP-C6VJ3RCH\SQLEXPRESS"
Db_name="KN16"
Db_driver="ODBC+Driver+17+for+SQL+Server"
#SQLALCHEMY_DATABASE_URI=f"mssql+pyodbc://{Server_name}/{Db_name}?driver={Db_driver}"
#SQLALCHEMY_DATABASE_URI="postgresql://kn16:W0BeMzCEoiKGX2zq8eQ8U9K4Hs9jnXeT@dpg-cj97cgavvtos73cff4jg-a.oregon-postgres.render.com/book_demo"
SQLALCHEMY_DATABASE_URI="postgresql://book_demo_z3hf_user:gqMU846RjallQRwztqkCFByejmiBhqUX@dpg-cvg0o05ds78s73fpg8vg-a/book_demo_z3hf"
def Set_config(app):
        app.config["SQLALCHEMY_DATABASE_URI"]=SQLALCHEMY_DATABASE_URI
        app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
