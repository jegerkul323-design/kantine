from flask import Flask, render_templates

app = Flask(__name__)

@app.route('/')
def index():
    return render_template("index.html")

@app.route('/meny')
def meny():
    return render_template("meny.html")

@app.route('/om')
def index():
    return render_template("om.html")

@app.route('/varer')
def index():
    return render_template("varer.html")

if __name__ == "__main__":
    app.run