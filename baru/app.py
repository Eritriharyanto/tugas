from flask import Flask
import requests

API_URL = "http://127.0.0.1:5000/"

app = Flask(__name__)

@app.get("/authors")
def authors():
    response = requests.get(API_URL + "author")
    if response.status_code != 200:
        return "Gagal mengambil data", 500
    authors = response.json()
    return """
    <title>Authors</title>
    <h1>Authors</h1>
    <hr>
    <ul>
    """ + ''.join([
        f"<li>{author['name']}</li>"
        for author in authors
    ]) + "</ul>"

@app.get("/publishers")
def publishers():
    response = requests.get(API_URL + "publisher")
    if response.status_code != 200:
        return "Gagal mengambil data", 500
    publishers = response.json()
    return """
    <title>Publishers</title>
    <h1>Publishers</h1>
    <hr>
    <table border="1">
    <tr>
        <th>Name</th>
        <th>City</th>
    </tr>
    """ + ''.join([
        f"""
        <tr>
            <td>{publisher['name']}</td>
            <td>{publisher['city']}</td>
        </tr>
        """
        for publisher in publishers
    ]) + "</table>"

@app.get("/books")
def books():
    response = requests.get(API_URL + "book")
    if response.status_code != 200:
        return "Gagal mengambil data", 500

    books = response.json()

    return """
    <html>
    <head>
        <title>Books</title>
        <style>
            body { font-family: Arial; padding: 20px; background: #f3f3f3; }
            h1 { color: #333; }
            table { 
                width: 100%; 
                border-collapse: collapse; 
                background: white;
                border-radius: 6px;
                overflow: hidden;
            }
            th { 
                background: #4CAF50; 
                color: white; 
                padding: 10px; 
                text-align: left;
            }
            td {
                padding: 10px; 
                border-bottom: 1px solid #ddd; 
            }
            tr:hover {
                background-color: #f1f1f1;
            }
        </style>
    </head>
    <body>
        <h1>Books</h1>
        <hr>

        <table>
            <tr>
                <th>Title</th>
                <th>Year</th>
                <th>Publisher</th>
                <th>Authors</th>
            </tr>
    """ + ''.join([
        f"""
            <tr>
                <td>{book['title']}</td>
                <td>{book['year']}</td>
                <td>{book['publisher']['name'] if book['publisher'] else '-'}</td>
                <td>{', '.join([a['name'] for a in book['authors']])}</td>
            </tr>
        """
        for book in books
    ]) + """
        </table>
    </body>
    </html>
    """


if __name__ == "__main__":
    app.run(debug=True, port=5001)
