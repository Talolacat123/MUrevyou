from flask import Flask, render_template, request
from database import *

app = Flask(__name__)
app.config['SECRET_KEY'] = 'sosecret'


@app.route("/")
def index():
    return render_template("index.html")

@app.route("/submit")
def submit():
    return render_template("form.html")

@app.route("/staffpicks")
def staffpicks():
    return render_template("staffpicks.html",albums = query_by_type("staff"))

@app.route("/studentpicks")
def studentpicks():
    return render_template("studentpicks.html", albums = query_by_type("student"))

@app.route("/form", methods = ['GET','POST'])
def homepage():
	if request.method=='GET':
		return render_template('form.html')
	else:
		print (request.form)
		sub_by = request.form["sub_by"]
		album_name = request.form["album_name"]
		artist = request.form["artist"]
		image_link = request.form["image_link"]
		about = request.form["about"]
		why_important = request.form["why_important"]
		stafforstudent = request.form["stafforstudent"]


		add_album(sub_by, album_name, artist, image_link, about, why_important, stafforstudent)
		return render_template("studentpicks.html",
		s = sub_by,  an = album_name, a = artist, il = image_link,ab = about, wi = why_important, sos = stafforstudent)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080, debug=True)
