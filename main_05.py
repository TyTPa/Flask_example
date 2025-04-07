from flask import Flask,render_template

app = Flask(__name__)

@app.route("/")
def hello_world():
    context = {
        "link": "Перейти "
    }
    return render_template("home.html", **context)

@app.route("/blog/")
def blog():
    context = {
        "link": "Перейти "
    }
    return render_template("about.html", **context)

if __name__ == "__main__":
    app.run()