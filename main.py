from flask import Flask, render_template, url_for

app = Flask(__name__)


@app.route('/')
@app.route('/home')
def index():
    return render_template("index.html")


@app.route('/about')
def about():
    return render_template("about.html")


@app.route('/CV')
def CV():
    return render_template("CV.html")


@app.route('/contact')
def contact():
    return render_template("contact.html")


@app.route('/myskills')
def myskills():
    return render_template("myskills.html")


@app.route('/myprojects')
def myprojects():
    return render_template("myprojects.html")


@app.route('/certificates')
def certificates():
    return render_template("certificates.html")





if __name__ == "__main__":
    app.run(debug=True)
