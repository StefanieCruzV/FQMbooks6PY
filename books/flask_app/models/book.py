from flask_app.config.mysqlconnection import connectToMySQL
from flask_app.models import author


class Book:
    def __init__(self, data):
        self.id = data['id']
        self.title = data['title']
        self.num_of_pages = data['num_of_pages']
        self.created_at = data['created_at']
        self.update_at = data['update_at']
        self.authors = []
    # Now we use class methods to query our database

    @classmethod
    def get_all(cls):
        query = "SELECT * FROM books;"
        results = connectToMySQL('books_schema').query_db(query)
        # guarda el resultado de la bd
        books = []
        # crea arreglo para guiardar los valores
        for book in results:  # itera los nombres de la base de datos
            books.append(cls(book))
            # flos mete en el arreglo -y los convierte en una clkase ususario
        return books

    @classmethod
    def get_by_id(cls, data):
        query = "SELECT * FROM favorites LEFT JOIN books ON book_id = books.id  LEFT JOIN users ON user_id = users.id WHERE books.id =%(id)s;"
        results = connectToMySQL('books_schema').query_db(query, data)
        book_ob = cls(results[0])  # primera parte
        for row_from_db in results:

            author_data = {
                "id": row_from_db["id"],
                "first_name": row_from_db["first_name"],
                "last_name": row_from_db["last_name"],
                "create_at": row_from_db["create_at"],
                "updated_at": row_from_db["updated_at"]
            }
            # vamos a meter el objeto ninja en el arreglo de objeto dojo
            book_ob.authors.append(author.Author(author_data))  # primera parte mas ninjas
        print(book_ob)

        return book_ob
