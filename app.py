from flask import Flask, render_template
from data import matvarer, dagmeny

app = Flask(__name__)

@app.route('/')
def index():
    return render_template("index.html")

@app.route('/meny')
def meny():
    return render_template("meny.html", dagmeny = dagmeny)

@app.route('/om')
def om():
    return render_template("om.html")

@app.route('/varer')
def varer():
    return render_template("varer.html", matvarer = matvarer)

if __name__ == "__main__":
    app.run()

    