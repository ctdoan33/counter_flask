from flask import Flask, render_template, request, redirect, session
app = Flask(__name__)
app.secret_key = "ThisIsSecret"
@app.route("/")
def countone():
    if "count" not in session:
        session["count"]=0
    session["count"]+=1
    return render_template("index.html")
@app.route("/two", methods=["POST"])
def counttwo():
    session["count"]+=1
    return redirect("/")
@app.route("/reset", methods=["POST"])
def reset():
    session["count"]=0
    return redirect("/")
app.run(debug=True)