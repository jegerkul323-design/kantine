from flask import Flask, render_template, request, redirect, session
from data import matvarer, dagmeny
import mysql.connector

app = Flask(__name__)
app.secret_key = "hemelig-nok"

def get_conn():
    return mysql.connector.connect(
        host = 'localhost', 
        user = 'theo', 
        password = 'Fli246&&',
        database = 'login'
    )

@app.route("/")
def index():
    return render_template("index.html")
    
@app.route("/register", methods = {"GET", "POST"})
def register():
    if request.method == "POST":
        navn = request.form["navn"]
        passord = request.form["passord"]
        brukernavn = request.form["brukernavn"]
        adresse = request.form["adresse"]

        conn = get_conn() #oppretter database forbindelse
        cur = conn.cursor() #cursor-objekt som skal sende spørringer til databasen
        cur.execute(
            'INSERT INTO brukere (navn, brukernavn, passord, adresse) VALUES (%s, %s, %s, %s)', 
            (navn, brukernavn, passord, adresse)
        )
        conn.commit()
        cur.close()
        conn.close()
        return redirect('/login')


    return render_template("register.html")

@app.route("/login", methods=["GET", "POST"])
def login():
    feil = None
    if request.method == "POST":
        brukernavn = request.form["brukernavn"]
        passord = request.form["passord"]

        conn = get_conn()
        cur = conn.cursor()
        cur.execute(
            "SELECT navn FROM brukere WHERE brukernavn=%s AND passord=%s",
            (brukernavn, passord)
        )
        user = cur.fetchone()
        cur.close()
        conn.close()

        if user:
            session["navn"] = user[0]
            return redirect("/welcome")
        else:
            feil = "Feil brukernavn eller passord"

    return render_template("login.html", feil=feil)

@app.route("/welcome")
def welcome():
    navn = session.get("navn")
    if not navn:
        return redirect("/login")
    return render_template("welcome.html", name=navn)

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