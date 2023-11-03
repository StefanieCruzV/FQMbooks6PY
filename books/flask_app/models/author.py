from flask_app.config.mysqlconnection import connectToMySQL
from flask_app.models import book


class Author:
    def __init__(self, data):
        # data = {'id': 1, 'first_name': 'Jane', 'last_name': 'Amsden', 'create_at': datetime.datetime(2022, 9, 6, 20, 37, 50), 'updated_at': datetime.datetime(2022, 9, 6, 20, 37, 50)}
        self.id = data['id']
        self.first_name = data['first_name']
        self.last_name = data['last_name']
        self.create_at = data['create_at']
        self.updated_at = data['updated_at']
        self.books = []

    # Now we use class methods to query our database

    @classmethod
    def get_all(cls):
        query = "SELECT * FROM users;"
        results = connectToMySQL('books_schema').query_db(query)
        # guarda el resultado de la bd
        print(results)
        authors = []
        # crea arreglo para guiardar los valores
        for author in results:  # itera los nombres de la base de datos
            authors.append(cls(author))
            # flos mete en el arreglo -y los convierte en una clkase ususario
        return authors
        

    @classmethod
    def save(cls, data):
        query = "INSERT INTO users ( first_name , last_name , create_at, updated_at ) VALUES ( %(first_name)s , %(last_name)s ,  NOW() , NOW() );"
        # los nombres deben ser los de la bd / los valores los del html
        print(query)
        return connectToMySQL('books_schema').query_db(query, data)

    @classmethod
    def get_by_id(cls, data):
        query = "SELECT * FROM favorites LEFT JOIN books ON book_id = books.id  LEFT JOIN users ON user_id = users.id WHERE users.id =%(id)s;"
        results = connectToMySQL('books_schema').query_db(query, data)
        print(results)
        author_ob = cls(results[0])  # primera parte
        for row_from_db in results:

            book_data = {
                "id": row_from_db["id"],
                "title": row_from_db["title"],
                "num_of_pages": row_from_db["num_of_pages"],
                "created_at": row_from_db["created_at"],
                "update_at": row_from_db["update_at"]
            }
            # vamos a meter el objeto ninja en el arreglo de objeto dojo
            author_ob.books.append(book.Book(book_data))  # primera parte mas ninjas

        return author_ob
