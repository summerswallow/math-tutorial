from flask import Flask, render_template
import algebra_builder as ab
app=Flask(__name__)

@app.route("/test")
def simplification1():
    return render_template("simplification1.html")
@app.route("/api")
def generate():
    
app.run()
