from flask import Flask, request, redirect
import requests

API_URL = "http://127.0.0.1:5000/"

app = Flask(__name__)

# menu = """
# <style>
#     .menu li{
#         display: block;
#         float: left;
#         padding: 0 1em;
#     }
#     .menu {
#         padding: 1em;
#     }
#     .menu + * {
#         clear: left;
#     }
# </style>
# <ul class="menu">
#     <li><a href="/authors">Authors</a></li>
#     <li><a href="/publishers">Publishers</a></li>
#     <li><a href="/books">Books</a></li>
#     <li><a href="/admin/authors">Author Management</a></li>
# </ul>
# <hr>
# """

menu = """
<style>
    .menu li{
        display: block;
        float: left;
        padding: 0 1em;
    }
    .menu {
        padding: 1em;
    }
    .menu + * {
        clear: left;
    }
</style>
<ul class="menu">
    <li><a href="/authors">Authors</a></li>
    <li><a href="/publishers">Publishers</a></li>
    <li><a href="/books">Books</a></li>
    <li><a href="/admin/authors">Author Management</a></li>
    <li><a href="/admin/books">Book Management</a></li>
</ul>
<hr>
"""

@app.get("/authors")
def authors():
    response = requests.get(API_URL + "author")
    if response.status_code != 200:
        return "Gagal mengambil data", 500
    authors = response.json()
    return f"""
    <title>Authors</title>
    {menu}
    <h1>Authors</h1>
    <hr>
    <ul>
    """ + ''.join([
        f"<li><a href='author/{author['id']}'>{author['name']}</a></li>"
        for author in authors
    ]) + "</ul>"

@app.get("/author/<id>")
def author(id):
    response = requests.get(API_URL + "author/" + id)
    if response.status_code != 200:
        return "Gagal mengambil data", 500
    author = response.json()
    css = "dt{float:left;width:100px}dd:before{content:':';padding:0 1em}"
    return f"""
    <title>Author Detail</title>
    <style>{css}</style>
    {menu}
    <h1>{author['name']}</h1>
    <hr>
    <dl>
        <dt>Name</dt><dd>{author['name']}</dd>
    </dl>
    """

@app.get("/publishers")
def publishers():
    response = requests.get(API_URL + "publisher")
    if response.status_code != 200:
        return "Gagal mengambil data", 500
    publishers = response.json()
    return f"""
    <title>Publishers</title>
    {menu}
    <h1>Publishers</h1>
    <hr>
    <table border="1">
    <tr>
        <th>Name</th>
        <th>City</th>
        <th>&nbsp;</th>
    </tr>
    """ + ''.join([
        f"""
        <tr>
            <td>{publisher['name']}</td>
            <td>{publisher['city']}</td>
            <th><a href="publisher/{publisher['id']}">Lihat</a></th>
        </tr>
        """
        for publisher in publishers
    ]) + "</table>"

@app.get("/publisher/<id>")
def publisher(id):
    response = requests.get(API_URL + "publisher/" + id)
    if response.status_code != 200:
        return "Gagal mengambil data", 500
    publisher = response.json()
    css = "dt{float:left;width:100px}dd:before{content:':';padding:0 1em}"
    return f"""
    <title>Publisher Detail</title>
    <style>{css}</style>
    {menu}
    <h1>{publisher['name']}</h1>
    <hr>
    <dl>
        <dt>Name</dt><dd>{publisher['name']}</dd>
        <dt>City</dt><dd>{publisher['city']}</dd>
    </dl>
    """

# tambahan
@app.get("/books")
def books():
    response = requests.get(API_URL + "book")
    if response.status_code != 200:
        return "Gagal mengambil data", 500

    books = response.json()
    return f"""
    <title>Books</title>
    {menu}
    <h1>Books</h1>
    <hr>
    <table border="1">
    <tr>
        <th>Title</th>
        <th>Year</th>
        <th>Publisher</th>
        <th>Authors</th>
        <th>&nbsp;</th>
    </tr>
    """ + "".join([
        f"""
        <tr>
            <td>{book['title']}</td>
            <td>{book['year']}</td>
            <td>{book['publisher']['name']}</td>
            <td>{", ".join(a['name'] for a in book['authors'])}</td>
            <td><a href="/book/{book['id']}">Lihat</a></td>
        </tr>
        """
        for book in books
    ]) + "</table>"

@app.get("/book/<id>")
def book(id):
    response = requests.get(API_URL + "book/" + id)
    if response.status_code != 200:
        return "Gagal mengambil data", 500

    book = response.json()
    css = "dt{float:left;width:100px}dd:before{content:':';padding:0 1em}"

    return f"""
    <title>Book Detail</title>
    <style>{css}</style>
    {menu}
    <h1>{book['title']}</h1>
    <hr>
    <dl>
        <dt>Title</dt><dd>{book['title']}</dd>
        <dt>Year</dt><dd>{book['year']}</dd>
        <dt>Publisher</dt><dd>{book['publisher']['name']}</dd>
        <dt>Authors</dt><dd>{", ".join(a['name'] for a in book['authors'])}</dd>
    </dl>
    """



@app.get("/admin/authors")
def admin_authors():
    response = requests.get(API_URL + "author")
    if response.status_code != 200:
        return "Gagal mengambil data", 500
    authors = response.json()
    return f"""
    <title>Author Management</title>
    {menu}
    <h1>Author Management</h1>
    <hr>
    <a href="/add/author">Add Author</a>
    <table border="1">
    <tr>
        <th>Name</th>
        <th>&nbsp;</th>
    </tr>
    """ + ''.join([
        f"""
        <tr>
            <td>{author['name']}</td>
            <td>
                <a href="/edit/author/{author['id']}">Edit</a>
                <a href="/delete/author/{author['id']}">Delete</a>
            </td>
        </tr>
        """
        for author in authors
    ]) + "</table>"

@app.route("/add/author", methods=["GET", "POST"])
def add_author():
    if request.method == "GET":
        return f"""
        <title>Add Author</title>
        {menu}
        <h1>Add Author</h1>
        <hr>
        <form method="POST">
            <p>
                Name<br>
                <input type="text" name="name">
            </p>
            <hr>
            <button type="submit">Simpan</button>
        </form>
        """
    else:
        name = request.form["name"]
        response = requests.post(API_URL + "author", json={
            "name": name
        })
        if response.status_code != 201:
            return "Gagal menambah data", 500
        return redirect("/admin/authors")

# tambahan
@app.get("/admin/books")
def admin_books():
    response = requests.get(API_URL + "book")
    if response.status_code != 200:
        return "Gagal mengambil data", 500

    books = response.json()
    return f"""
    <title>Book Management</title>
    {menu}
    <h1>Book Management</h1>
    <hr>
    <a href="/add/book">Add Book</a>
    <table border="1">
    <tr>
        <th>Title</th>
        <th>&nbsp;</th>
    </tr>
    """ + "".join([
        f"""
        <tr>
            <td>{book['title']}</td>
            <td>
                <a href="/edit/book/{book['id']}">Edit</a>
                <a href="/delete/book/{book['id']}">Delete</a>
            </td>
        </tr>
        """
        for book in books
    ]) + "</table>"

@app.route("/add/book", methods=["GET", "POST"])
def add_book():
    if request.method == "GET":
        authors = requests.get(API_URL + "author").json()
        publishers = requests.get(API_URL + "publisher").json()

        return f"""
        <title>Add Book</title>
        {menu}
        <h1>Add Book</h1>
        <hr>
        <form method="POST">
            <p>Title<br><input type="text" name="title"></p>
            <p>Year<br><input type="number" name="year"></p>

            <p>Publisher<br>
            <select name="publisher_id">
                {''.join(f"<option value='{p['id']}'>{p['name']}</option>" for p in publishers)}
            </select>
            </p>

            <p>Authors<br>
            {''.join(f"<input type='checkbox' name='author_ids' value='{a['id']}'> {a['name']}<br>" for a in authors)}
            </p>

            <hr>
            <button type="submit">Simpan</button>
        </form>
        """
    else:
        response = requests.post(API_URL + "book", json={
            "title": request.form["title"],
            "year": int(request.form["year"]),
            "publisher_id": int(request.form["publisher_id"]),
            "author_ids": list(map(int, request.form.getlist("author_ids")))
        })

        if response.status_code != 201:
            return "Gagal menambah data", 500

        return redirect("/admin/books")

@app.route("/delete/book/<id>", methods=["GET", "POST"])
def delete_book(id):
    if request.method == "GET":
        book = requests.get(API_URL + "book/" + id).json()
        return f"""
        <title>Delete Book</title>
        {menu}
        <h1>{book['title']}</h1>
        <p>Apakah Anda yakin ingin menghapus buku ini?</p>
        <form method="POST">
            <button type="submit">Delete</button>
        </form>
        """
    else:
        requests.delete(API_URL + "book/" + id)
        return redirect("/admin/books")
    
@app.route("/edit/book/<id>", methods=["GET", "POST"])
def edit_book(id):
    if request.method == "GET":
        book = requests.get(API_URL + "book/" + id).json()
        authors = requests.get(API_URL + "author").json()
        publishers = requests.get(API_URL + "publisher").json()

        return f"""
        <title>Edit Book</title>
        {menu}
        <h1>Edit Book</h1>
        <form method="POST">
            <p>
                Title<br>
                <input type="text" name="title" value="{book['title']}">
            </p>

            <p>
                Year<br>
                <input type="number" name="year" value="{book['year']}">
            </p>

            <p>
                Publisher<br>
                <select name="publisher_id">
                    {''.join(
                        f"<option value='{p['id']}' {'selected' if p['id']==book['publisher']['id'] else ''}>{p['name']}</option>"
                        for p in publishers
                    )}
                </select>
            </p>

            <p>
                Authors<br>
                {''.join(
                    f"<input type='checkbox' name='author_ids' value='{a['id']}' {'checked' if a['id'] in [x['id'] for x in book['authors']] else ''}> {a['name']}<br>"
                    for a in authors
                )}
            </p>

            <hr>
            <button type="submit">Save</button>
        </form>
        """


@app.route("/delete/author/<id>", methods=["GET", "POST"])
def delete_author(id):
    if request.method == "GET":
        response = requests.get(API_URL + "author/" + id)
        if response.status_code != 200:
            return "Gagal mengambil data", 500
        author = response.json()
        css = "dt{float:left;width:100px}dd:before{content:':';padding:0 1em}"
        return f"""
        <title>Delete Author</title>
        <style>{css}</style>
        {menu}
        <h1>{author['name']}</h1>
        <hr>
        <dl>
            <dt>Name</dt><dd>{author['name']}</dd>
        </dl>
        <form method="POST">
            <p>Apakah Anda benar-benar mau menghapus author ini?</p>
            <hr>
            <button type="submit">Delete</button>
        </form>
        """
    else:
        response = requests.delete(API_URL + "author/" + id)
        if response.status_code != 200:
            return "Gagal menghapus data", 500
        return redirect("/admin/authors")

@app.route("/edit/author/<id>", methods=["GET", "POST"])
def edit_author(id):
    if request.method == "GET":
        response = requests.get(API_URL + "author/" + id)
        if response.status_code != 200:
            return "Gagal mengambil data", 500
        author = response.json()
        return f"""
        <title>Edit Author</title>
        {menu}
        <h1>{author['name']}</h1>
        <form method="POST">
            <p>
                Name<br>
                <input type="text" name="name" value="{author['name']}">
            </p>
            <hr>
            <button type="submit">Save</button>
        </form>
        """
    else:
        name = request.form["name"]
        response = requests.put(API_URL + "author/" + id, json={
            "name": name
        })
        if response.status_code != 200:
            return "Gagal mengedit data", 500
        return redirect("/admin/authors")

if __name__ == "__main__":
    app.run(debug=True, port=5001)