from flask import Flask, render_template

app=Flask(__name__)

@app.route("/test")
def simplification1():
    return render_template("simplification1.html")

app.run()
