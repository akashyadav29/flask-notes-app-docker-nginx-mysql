from flask import Flask, render_template, request, redirect
import mysql.connector
import time
import os

app = Flask(__name__)

while True:
    try:
        db = mysql.connector.connect(
            host=os.getenv("MYSQL_HOST"),
            user="root",
            password=os.getenv("MYSQL_ROOT_PASSWORD"),
            database=os.getenv("MYSQL_DATABASE")
        )
        break
    except:
        print("Waiting for MySQL...")
        time.sleep(5)

cursor = db.cursor()

@app.route("/")
def index():
    cursor.execute("SELECT * FROM notes")
    notes = cursor.fetchall()
    return render_template("index.html", notes=notes)

@app.route("/add", methods=["POST"])
def add():
    note = request.form["note"]
    color = request.form["color"]

    cursor.execute(
        "INSERT INTO notes (content,color) VALUES (%s,%s)",
        (note,color)
    )

    db.commit()

    return redirect("/")

@app.route("/delete/<int:id>")
def delete(id):

    cursor.execute("DELETE FROM notes WHERE id=%s",(id,))
    db.commit()

    return redirect("/")

if __name__ == "__main__":
    app.run(host="0.0.0.0",port=5000)
