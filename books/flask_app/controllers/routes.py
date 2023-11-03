from crypt import methods
from flask_app import app
from flask import render_template,redirect,request,session
from flask_app.models.author import Author
from flask_app.models.book import Book
from flask_app.models.favorites import Favorites

@app.route("/")
def index():
    books = Book.get_all() # regresa los valores del metodo get all y almacena todos los datos de lbd
    print(books)
    return render_template("books.html",books=books) 


@app.route("/add_book", methods=["POST"])
def add_book():
    data = {
        "title":request.form["title"],
        "num_of_pages": int(request.form["num_of_pages"]),
        # guarda los valores del formulario
        }
    print(data)
    id =Book.save(data) # manda llamar al metodo para guardar
    print(id)
    return redirect("/") 

@app.route("/get_authors")
def get_authors():
    authors = Author.get_all() # regresa los valores del metodo get all y almacena todos los datos de lbd
    print(authors)
    return render_template("authors.html",authors=authors) 


@app.route("/add_author", methods=["POST"])
def add_author():
    data = {
        "first_name":request.form["first_name"],
        "last_name":request.form["last_name"]
        # guarda los valores del formulario
        }
    id =Author.save(data) # manda llamar al metodo para guardar
    return redirect("/get_authors") 

@app.route("/show_authors/<int:id>")
def show_authors(id):
    data = {
        "id": id
        }
    author = Author.get_by_id(data)
    books=Book.get_all()
    return render_template("authorshow.html",author=author, books=books)

@app.route("/add_book_author/<int:author_id>",methods=["POST"] )
def add_book_author(author_id):
    data = {
        "user_id": author_id,
        "book_id": int(request.form["location"])
        }
    Favorites.insert_favorites(data)
   
    return redirect(f"/show_authors/{author_id}")



@app.route("/show_books/<int:book_id>")
def get_books_by_id(book_id):
    data = {
        "id": book_id,
        }
    book_obj = Book.get_by_id(data) # regresa los valores del metodo get all y almacena todos los datos de lbd
    authors = Author.get_all()
    return render_template("bookshow.html", book_obj=book_obj, authors=authors)    

@app.route("/add_author_book/<int:book_id>",methods=["POST"] )
def add_author_book(book_id):
    data = {
        "book_id": book_id,
        "user_id": int(request.form["location"])
        }
    Favorites.insert_favorites(data)

    return redirect(f"/show_books/{book_id}")


# @app.route('/show_author/<int:id>')
# def show_author(id):
#     print(id)
#     data = {
#         "id": id
#         }
#     print(data)
#     authors = Author .get__by_dojoid(data)
#     print(dojo_ninjas.ninjas)
#     return render_template("show.html",dojo_ninjas=dojo_ninjas) 









# @app.route("/newuser")
# def newuser():
#     return render_template("newuser.html")
 
 

# @app.route('/create_user', methods=["POST"])
# def create_user():
#     data = {
#         "uname": request.form["uname"],
#         "ulastname": request.form["ulastname"],
#         "uemail": request.form["uemail"]
#         # guarda los valores del formulario
#         }
   
#     id=User.save(data) # manda llamar al metodo para guardar
#     print(id)
   
#     return redirect(f"/show_user/{id}")# lo que me regreso de la base al html
#         # si es otra pagina 

# @app.route('/delete_user/<int:id>')
# def delete_user(id):
#     print(id)
#     data = {
#         "id": id
#         }
#     User.delete(data)
#     users = User.get_all()
#     return render_template("users.html",users=users)
   


# @app.route('/show_user/<int:id>')
# def show_user(id):
#     print(id)
#     data = {
#         "id": id,
    
#         }
#     user_id = User.get_user_by_id(data)
#     print(user_id)
#     return render_template("showuser.html",user= user_id) # lo que me regreso de la base al html
#         # si es otra pagina 

# @app.route('/update_user/<int:id>')
# def update_user(id):
#     print(id)
#     data = {
#         "id": id
#         }
#     user_id = User.get_user_by_id(data)
#     print(user_id)
#     return render_template("updateuser.html",user_id= user_id) # lo que me regreso de la base al html
#         # si es otra pagina 

# @app.route('/update_user/<int:id>', methods=["POST"])
# def update_user_post(id):
#     print(id)
#     data = {
#         "id": id,
#         "uname": request.form["uname"],
#         "ulastname": request.form["ulastname"],
#         "uemail": request.form["uemail"]
#         }
#     User.update(data)
#     print(f"/show_user/{id}")
#     return redirect(f"/show_user/{id}") # lo que me regreso de la base al html
#         # si es otra pagina 