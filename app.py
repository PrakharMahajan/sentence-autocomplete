from flask import Flask, request, render_template

app = Flask('__name__')


@app.route("/", methods=["POST", "GET"])
def home():
    if request.method == "GET":
        languages = ["C++", "Python", "PHP", "Java", "C", "Ruby", "R", "C#", "Dart", "Fortran", "Pascal", "JavaScript",
                     "CSS", "HTML", "RaspberryPi", "PROLOG", "Go", "Swift", "Kotlin", "MATLAB", "Rust", "Scala"]
        return render_template("index.html", languages=languages)

