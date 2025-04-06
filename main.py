from flask import Flask,render_template

app = Flask(__name__)

@app.route("/")
def hello_world():
    return render_template("index.html") # Внутри () пишем название html-файла в кавычках

@app.route("/blog/")
def blog():
    return render_template("blogs.html")

@app.route("/contacts/")
def contacts():
    return render_template("contacts.html")

if __name__ == "__main__":
    app.run()