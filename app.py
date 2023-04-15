from flask import Flask, render_template

app = Flask(__name__)


@app.route("/")
def landing_page():
  return render_template('home.html')


@app.route("/questions")
def questions():
  return render_template('questions.html')


@app.route("/bcounselor")
def bcounselor():
  return render_template('bcounselor.html')


if __name__ == "__main__":
  app.run(host='0.0.0.0', debug=True)
