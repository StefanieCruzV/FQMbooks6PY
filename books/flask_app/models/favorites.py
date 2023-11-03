from flask_app.config.mysqlconnection import connectToMySQL

class Favorites:
    def __init__(self, data):
        self.user_id = data['user_id']
        self.user_book= data['user_book']


    @classmethod
    def insert_favorites(cls,data):
        query = "INSERT INTO  favorites ( user_id , book_id) VALUES (%(user_id)s,%(book_id)s);"
        results = connectToMySQL('books_schema').query_db(query,data)
        # guarda el resultado de la bd 
