from flask import Flask, render_template, request, jsonify
from database import add_counselor_to_db, load_counselors_from_db, selected_counselor_from_db, add_answers_to_db

app = Flask(__name__)


@app.route("/")
def landing_page():
  return render_template('home.html')


@app.route("/visualization")
def visualization():
  return render_template('visualization.html')


@app.route("/self-help")
def self_help():
  return render_template('self_help.html')


@app.route("/counselor-register")
def counselor():
  return render_template("counselor_registration.html")


@app.route("/counselor/registered", methods=['post'])
def register_as_counselor():
  data = request.form
  add_counselor_to_db(data)
  return render_template(
    'counselor_registered.html',
    counselor=data,
  )


@app.route("/questions")
def questions():
  return render_template("questions.html")


@app.route("/questions/answers", methods=['post'])
def answers():
  data = request.form
  add_answers_to_db(data)
  return render_template('answers.html', answers=data)


@app.route("/select_counselor")
def select_counselor():
  counselors = load_counselors_from_db()
  return render_template('select_counselor.html', counselors=counselors)


@app.route("/counselor/<counselor_name>")
def show_counselor(counselor_name):
  counselor = selected_counselor_from_db(counselor_name)
  if not counselor:
    return "Not Found", 404

  return render_template('counselor_page.html', counselor=counselor)


# @app.route("/available_counselors", methods=['post'])
# def available_counselors():
#   gender = request.form['gender']
#   counselors = load_available_counselors_from_db(gender)
#   return render_template('available_counselors.html', counselors=counselors)


@app.route("/api/counselors")
def show_counselors():
  counselors = load_counselors_from_db()
  return jsonify(counselors)


@app.route("/api/answers", methods=['GET', 'POST'])
def show_answers():
  if request.method == 'POST':
    answers = dict(request.form)
    return jsonify(answers)
  else:
    # Handle GET requests
    return render_template("answers.html")


@app.route("/contact-us")
def contact_us():
  return render_template('contact_us.html')


if __name__ == "__main__":
  app.run(host='0.0.0.0', debug=True)
