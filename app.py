from flask import Flask, render_template, request, jsonify
from database import add_counselor_to_db

app = Flask(__name__)


@app.route("/")
def landing_page():
  return render_template('home.html')


@app.route("/questions")
def questions():
  return render_template("questions.html")


@app.route("/counselor")
def counselor():
  return render_template("counselor.html")



@app.route("/counselor/registered", methods=['post'])
def register_as_counselor():
  data = request.form
  add_counselor_to_db(data)
  return render_template('counselor_registered.html', 
                         counselor=data,
                         )


# @app.route("/api/counselor-registered")
# def


if __name__ == "__main__":
  app.run(host='0.0.0.0', debug=True)
