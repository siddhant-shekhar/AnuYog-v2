from flask import Flask, render_template, request, jsonify, url_for, redirect, session, g
from flask_sqlalchemy import SQLAlchemy
import bcrypt

app = Flask(__name__)

####################################################################################################################

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database.db'

db = SQLAlchemy(app)
app.secret_key = 'secret_key'


class userHero(db.Model):
  id = db.Column(db.Integer, primary_key=True)
  name = db.Column(db.String(100), nullable=False)
  email = db.Column(db.String(100), nullable=False)
  password = db.Column(db.String(100), nullable=False)
  #question and answer
  Q1A = db.Column(db.Integer)
  Q2A = db.Column(db.Integer)
  Q3A = db.Column(db.Integer)
  Q4A = db.Column(db.Integer)
  Q5A = db.Column(db.Integer)
  Q6A = db.Column(db.Integer)
  Q7A = db.Column(db.Integer)
  Q8A = db.Column(db.Integer)
  Q9A = db.Column(db.Integer)
  Q10A = db.Column(db.Integer)
  Q11A = db.Column(db.Integer)
  Q12A = db.Column(db.Integer)
  Q13A = db.Column(db.Integer)
  Q14A = db.Column(db.Integer)
  Q15A = db.Column(db.Integer)
  Q16A = db.Column(db.Integer)
  Q17A = db.Column(db.Integer)
  Q18A = db.Column(db.Integer)
  Q19A = db.Column(db.Integer)
  Q20A = db.Column(db.Integer)
  Q21A = db.Column(db.Integer)
  Q22A = db.Column(db.Integer)
  Q23A = db.Column(db.Integer)
  Q24A = db.Column(db.Integer)
  Q25A = db.Column(db.Integer)
  Q26A = db.Column(db.Integer)
  Q27A = db.Column(db.Integer)
  Q28A = db.Column(db.Integer)
  Q29A = db.Column(db.Integer)
  Q30A = db.Column(db.Integer)
  Q31A = db.Column(db.Integer)
  Q32A = db.Column(db.Integer)
  Q33A = db.Column(db.Integer)
  Q34A = db.Column(db.Integer)
  Q35A = db.Column(db.Integer)
  Q36A = db.Column(db.Integer)
  Q37A = db.Column(db.Integer)
  Q38A = db.Column(db.Integer)
  Q39A = db.Column(db.Integer)
  Q40A = db.Column(db.Integer)
  Q41A = db.Column(db.Integer)
  Q42A = db.Column(db.Integer)
  TIPI1 = db.Column(db.Integer)
  TIPI2 = db.Column(db.Integer)
  TIPI3 = db.Column(db.Integer)
  TIPI4 = db.Column(db.Integer)
  TIPI5 = db.Column(db.Integer)
  TIPI6 = db.Column(db.Integer)
  TIPI7 = db.Column(db.Integer)
  TIPI8 = db.Column(db.Integer)
  TIPI9 = db.Column(db.Integer)
  TIPI10 = db.Column(db.Integer)
  education = db.Column(db.Integer)
  urban = db.Column(db.Integer)
  gender = db.Column(db.Integer)
  married = db.Column(db.Integer)
  familysize = db.Column(db.Integer)
  age_group = db.Column(db.Integer)
  about = db.Column(db.String(1000))

  # d_result = db.Column(db.String(100))
  # a_result = db.Column(db.String(100))
  # s_result = db.Column(db.String(100))
  # suicidal_result = db.Column(db.String(100))

  def __init__(self, name, email, password):
    self.name = name
    self.email = email
    self.password = bcrypt.hashpw(password.encode('utf-8'),
                                  bcrypt.gensalt()).decode('utf-8')

  def check_password(self, password):
    return bcrypt.checkpw(password.encode('utf-8'),
                          self.password.encode('utf-8'))

  def update_answers(self, Q1A, Q2A, Q3A, Q4A, Q5A, Q6A, Q7A, Q8A, Q9A, Q10A,
                     Q11A, Q12A, Q13A, Q14A, Q15A, Q16A, Q17A, Q18A, Q19A,
                     Q20A, Q21A, Q22A, Q23A, Q24A, Q25A, Q26A, Q27A, Q28A,
                     Q29A, Q30A, Q31A, Q32A, Q33A, Q34A, Q35A, Q36A, Q37A,
                     Q38A, Q39A, Q40A, Q41A, Q42A):
    self.Q1A = Q1A
    self.Q2A = Q2A
    self.Q3A = Q3A
    self.Q4A = Q4A
    self.Q5A = Q5A
    self.Q6A = Q6A
    self.Q7A = Q7A
    self.Q8A = Q8A
    self.Q9A = Q9A
    self.Q10A = Q10A
    self.Q11A = Q11A
    self.Q12A = Q12A
    self.Q13A = Q13A
    self.Q14A = Q14A
    self.Q15A = Q15A
    self.Q16A = Q16A
    self.Q17A = Q17A
    self.Q18A = Q18A
    self.Q19A = Q19A
    self.Q20A = Q20A
    self.Q21A = Q21A
    self.Q22A = Q22A
    self.Q23A = Q23A
    self.Q24A = Q24A
    self.Q25A = Q25A
    self.Q26A = Q26A
    self.Q27A = Q27A
    self.Q28A = Q28A
    self.Q29A = Q29A
    self.Q30A = Q30A
    self.Q31A = Q31A
    self.Q32A = Q32A
    self.Q33A = Q33A
    self.Q34A = Q34A
    self.Q35A = Q35A
    self.Q36A = Q36A
    self.Q37A = Q37A
    self.Q38A = Q38A
    self.Q39A = Q39A
    self.Q40A = Q40A
    self.Q41A = Q41A
    self.Q42A = Q42A

  def update_answers1(self, TIPI1, TIPI2, TIPI3, TIPI4, TIPI5, TIPI6, TIPI7,
                      TIPI8, TIPI9, TIPI10):
    self.TIPI1 = TIPI1
    self.TIPI2 = TIPI2
    self.TIPI3 = TIPI3
    self.TIPI4 = TIPI4
    self.TIPI5 = TIPI5
    self.TIPI6 = TIPI6
    self.TIPI7 = TIPI7
    self.TIPI8 = TIPI8
    self.TIPI9 = TIPI9
    self.TIPI10 = TIPI10

  def update_answers2(self, education, urban, gender, married, familysize,
                      age_group, about):
    self.education = education
    self.urban = urban
    self.gender = gender
    self.married = married
    self.familysize = familysize
    self.age_group = age_group
    self.about = about

  # def update_results(self, d_result, a_result, s_result, suicidal_result):
  #   self.d_result = d_result
  #   self.a_result = a_result
  #   self.s_result = s_result
  #   self.suicidal_result = suicidal_result


class userCounselor(db.Model):
  id = db.Column(db.Integer, primary_key=True)
  email = db.Column(db.String(100), nullable=False)
  name = db.Column(db.String(100), nullable=False)
  password = db.Column(db.String(100), nullable=False)
  gender = db.Column(db.String(100), nullable=False)
  age = db.Column(db.String(100), nullable=False)
  occupation = db.Column(db.String(100), nullable=False)
  time = db.Column(db.String(100), nullable=False)
  phone_no = db.Column(db.String(100), nullable=False)
  about = db.Column(db.String(1000), nullable=False)

  def __init__(self, email, name, password, gender, age, occupation, time,
               phone_no, about):
    self.email = email
    self.name = name
    self.password = bcrypt.hashpw(password.encode('utf-8'),
                                  bcrypt.gensalt()).decode('utf-8')
    self.gender = gender
    self.age = age
    self.occupation = occupation
    self.time = time
    self.phone_no = phone_no
    self.about = about

  def check_password(self, password):
    return bcrypt.checkpw(password.encode('utf-8'),
                          self.password.encode('utf-8'))


with app.app_context():
  db.create_all()

####################################################################################################################


@app.route("/visualization")
def visualization():
  user = None
  user1 = None
  if 'email' in session:
    user = userHero.query.filter_by(email=session['email']).first()
    user1 = userCounselor.query.filter_by(email=session['email']).first()

  if user:
    return render_template('visualization.html', user=user)
  else:
    return render_template('visualization.html', user=user1)


@app.route("/contact-us")
def contact_us():
  user = None
  user1 = None
  if 'email' in session:
    user = userHero.query.filter_by(email=session['email']).first()
    user1 = userCounselor.query.filter_by(email=session['email']).first()

  if user:
    return render_template('contact_us.html', user=user)
  else:
    return render_template('contact_us.html', user=user1)


@app.route("/self-help")
def self_help():
  user = None
  user1 = None
  if 'email' in session:
    user = userHero.query.filter_by(email=session['email']).first()
    user1 = userCounselor.query.filter_by(email=session['email']).first()

  if user:
    return render_template('self_help.html', user=user)
  else:
    return render_template('self_help.html', user=user1)


@app.route("/login")
def login():
  return render_template('login.html')


###############################################################


@app.route("/register_hero", methods=['GET', 'POST'])
def register_hero():
  if request.method == 'POST':
    name = request.form['name']
    email = request.form['email']
    password = request.form['password']

    new_user = userHero(email=email, password=password, name=name)

    db.session.add(new_user)
    db.session.commit()

    return redirect(url_for('login_hero'))

  return render_template('hero_register.html')


@app.route("/login_hero", methods=['GET', 'POST'])
def login_hero():
  if request.method == 'POST':
    email = request.form['email']
    password = request.form['password']

    user = userHero.query.filter_by(email=email).first()

    if user and user.check_password(password):
      session['email'] = user.email

      return redirect(url_for('landing_page'))

    else:
      return render_template('hero_login.html',
                             error='Invalid email or password, try again')

  return render_template('hero_login.html')


@app.route("/register_counselor", methods=['GET', 'POST'])
def register_counselor():
  if request.method == 'POST':
    name = request.form['name']
    email = request.form['email']
    password = request.form['password']
    gender = request.form['gender']
    age = request.form['age']
    occupation = request.form['occupation']
    time = request.form['time']
    phone_no = request.form['phone_no']
    about = request.form['about']

    new_user = userCounselor(email=email,
                             password=password,
                             name=name,
                             gender=gender,
                             age=age,
                             occupation=occupation,
                             time=time,
                             phone_no=phone_no,
                             about=about)

    db.session.add(new_user)
    db.session.commit()

    return redirect(url_for('login_counselor'))

  return render_template('counselor_register.html')


@app.route("/login_counselor", methods=['GET', 'POST'])
def login_counselor():
  if request.method == 'POST':
    email = request.form['email']
    password = request.form['password']

    user = userCounselor.query.filter_by(email=email).first()

    if user and user.check_password(password):
      session['email'] = user.email

      return redirect(url_for('landing_page'))

    else:
      return render_template('counselor_login.html',
                             error='Invalid email or password, try again')

  return render_template('counselor_login.html')


@app.route('/logout')
def logout():
  session.pop('email', None)
  return redirect('/')


# @app.route("/counselor/registered", methods=['post'])
# def register_as_counselor():
#   data = request.form
#   add_counselor_to_db(data)
#   return render_template(
#     'counselor_registered.html',
#     counselor=data,
#   )


@app.route("/")
def landing_page():
  user = None
  user1 = None
  if 'email' in session:
    user = userHero.query.filter_by(email=session['email']).first()
    user1 = userCounselor.query.filter_by(email=session['email']).first()

  if user:
    return render_template('home.html', user=user)
  else:
    return render_template('home.html', user=user1)


@app.route("/questions", methods=['GET', 'POST'])
def questions():
  user = None
  user1 = None
  if 'email' in session:
    user = userHero.query.filter_by(email=session['email']).first()
    user1 = userCounselor.query.filter_by(email=session['email']).first()

  if user:
    if request.method == 'POST':
      Q1A = request.form['Q1A']
      Q2A = request.form['Q2A']
      Q3A = request.form['Q3A']
      Q4A = request.form['Q4A']
      Q5A = request.form['Q5A']
      Q6A = request.form['Q6A']
      Q7A = request.form['Q7A']
      Q8A = request.form['Q8A']
      Q9A = request.form['Q9A']
      Q10A = request.form['Q10A']
      Q11A = request.form['Q11A']
      Q12A = request.form['Q12A']
      Q13A = request.form['Q13A']
      Q14A = request.form['Q14A']
      Q15A = request.form['Q15A']
      Q16A = request.form['Q16A']
      Q17A = request.form['Q17A']
      Q18A = request.form['Q18A']
      Q19A = request.form['Q19A']
      Q20A = request.form['Q20A']
      Q21A = request.form['Q21A']
      Q22A = request.form['Q22A']
      Q23A = request.form['Q23A']
      Q24A = request.form['Q24A']
      Q25A = request.form['Q25A']
      Q26A = request.form['Q26A']
      Q27A = request.form['Q27A']
      Q28A = request.form['Q28A']
      Q29A = request.form['Q29A']
      Q30A = request.form['Q30A']
      Q31A = request.form['Q31A']
      Q32A = request.form['Q32A']
      Q33A = request.form['Q33A']
      Q34A = request.form['Q34A']
      Q35A = request.form['Q35A']
      Q36A = request.form['Q36A']
      Q37A = request.form['Q37A']
      Q38A = request.form['Q38A']
      Q39A = request.form['Q39A']
      Q40A = request.form['Q40A']
      Q41A = request.form['Q41A']
      Q42A = request.form['Q42A']

      user.update_answers(Q1A, Q2A, Q3A, Q4A, Q5A, Q6A, Q7A, Q8A, Q9A, Q10A,
                          Q11A, Q12A, Q13A, Q14A, Q15A, Q16A, Q17A, Q18A, Q19A,
                          Q20A, Q21A, Q22A, Q23A, Q24A, Q25A, Q26A, Q27A, Q28A,
                          Q29A, Q30A, Q31A, Q32A, Q33A, Q34A, Q35A, Q36A, Q37A,
                          Q38A, Q39A, Q40A, Q41A, Q42A)

      db.session.commit()

      return redirect(url_for('questions1'))
  else:
    return render_template('counselor_access_denied_questions.html',
                           user=user1)
  return render_template('questions.html', user=user)


@app.route("/questions1", methods=['GET', 'POST'])
def questions1():
  user = None
  user1 = None
  if 'email' in session:
    user = userHero.query.filter_by(email=session['email']).first()
    user1 = userCounselor.query.filter_by(email=session['email']).first()

  if user:
    if request.method == 'POST':
      TIPI1 = request.form['TIPI1']
      TIPI2 = request.form['TIPI2']
      TIPI3 = request.form['TIPI3']
      TIPI4 = request.form['TIPI4']
      TIPI5 = request.form['TIPI5']
      TIPI6 = request.form['TIPI6']
      TIPI7 = request.form['TIPI7']
      TIPI8 = request.form['TIPI8']
      TIPI9 = request.form['TIPI9']
      TIPI10 = request.form['TIPI10']

      user.update_answers1(TIPI1, TIPI2, TIPI3, TIPI4, TIPI5, TIPI6, TIPI7,
                           TIPI8, TIPI9, TIPI10)

      db.session.commit()

      return redirect(url_for('questions2'))
  else:
    return render_template('counselor_access_denied_questions.html',
                           user=user1)
  return render_template('questions1.html', user=user)


@app.route("/questions2", methods=['GET', 'POST'])
def questions2():
  user = None
  user1 = None
  if 'email' in session:
    user = userHero.query.filter_by(email=session['email']).first()
    user1 = userCounselor.query.filter_by(email=session['email']).first()

  if user:
    if request.method == 'POST':
      education = request.form['education']
      urban = request.form['urban']
      gender = request.form['gender']
      married = request.form['married']
      familysize = request.form['familysize']
      age_group = request.form['age_group']
      about = request.form['about']

      user.update_answers2(education, urban, gender, married, familysize,
                           age_group, about)

      db.session.commit()

      return redirect(url_for('landing_page'))
  else:
    return render_template('counselor_access_denied_questions.html',
                           user=user1)
  return render_template('questions2.html', user=user)


# @app.route("/result", methods=['post'])
# def result():
#   data = request.form
#   add_answers_to_db(data)
#   return render_template('result.html', answers=data)

# @app.route("/select_counselor")
# def select_counselor():
#   ages = load_distinct_age_from_db()
#   genders = load_distinct_gender_from_db()
#   time = load_distinct_time_from_db()
#   return render_template('select_counselor.html',
#                          ages=ages,
#                          genders=genders,
#                          time=time)

# @app.route("/available_counselors", methods=['post', 'get'])
# def available_counselors():
#   gender = request.form['gender']
#   age = request.form['age']
#   time = request.form['time']
#   counselors = load_available_counselors_from_db(gender, age, time)
#   return render_template('available_counselors.html', counselors=counselors)


@app.route("/counselor/profile")
def user_profile():
  user = None
  user1 = None
  if 'email' in session:
    user = userHero.query.filter_by(email=session['email']).first()
    user1 = userCounselor.query.filter_by(email=session['email']).first()

  if user:
    return render_template('profile_hero.html',
                           user=user,
                           dass=convert.dass,
                           tipi=convert.tipi,
                           edu=convert.edu,
                           urban=convert.urban,
                           gender=convert.gender,
                           married=convert.married,
                           age=convert.age)
  else:
    return render_template('profile_counselor.html', user=user1)


####################################################################################################################


@app.route("/trial")
def trial():
  return render_template('select_counselor.html')


# @app.route("/api/answers", methods=['GET', 'POST'])
# def show_answers():
#   if request.method == 'POST':
#     answers = dict(request.form)
#     return jsonify(answers)
#   else:
#     # Handle GET requests
#     return render_template("home.html")


@app.route("/api/userHero_table", methods=['GET', 'POST'])
def show_table():
  user_data = userHero.query.all()

  all_rows = []
  for row in user_data:
    row_dict = row.__dict__
    row_dict.pop('_sa_instance_state', None)
    all_rows.append(row_dict)

  return jsonify(all_rows)


@app.route("/api/userCounselor_table", methods=['GET', 'POST'])
def show_table1():
  user_data = userCounselor.query.all()

  all_rows = []
  for row in user_data:
    row_dict = row.__dict__
    row_dict.pop('_sa_instance_state', None)
    all_rows.append(row_dict)

  return jsonify(all_rows)


# @app.route("/api/counselors")
# def show_counselors():
#   counselors = load_counselors_from_db()
#   return jsonify(counselors)

# @app.route("/api/time", methods=['post', 'get'])
# def show_gender():
#   gender = request.form['gender']
#   age = request.form['age']
#   time = request.form['time']
#   answer = load_available_counselors_from_db(gender, age, time)
#   return jsonify(answer)

# @app.route("/api/name/<name>")
# def name(name):
#   name = dict(selected_counselor_from_db(name))
#   return jsonify(name)


class convert():

  def dass(value):
    if value == 0:
      return "Did not apply to me at all"
    elif value == 1:
      return "Applied to me to some degree, or some of the time"
    elif value == 2:
      return "Applied to me to a considerable degree, or a good part of the time"
    elif value == 3:
      return "Applied to me very much, or most of the time"

  def tipi(value):
    if value == 1:
      return "Disagree strongly"
    elif value == 2:
      return "Disagree moderately"
    elif value == 3:
      return "Disagree a little"
    elif value == 4:
      return "Neither agree nor disagree"
    elif value == 5:
      return "Agree a little"
    elif value == 6:
      return "Agree moderately"
    elif value == 7:
      return "Agree strongly"

  def edu(value):
    if value == 1:
      return "Less than hogh school"
    elif value == 2:
      return "High school"
    elif value == 3:
      return "University Degree"
    elif value == 4:
      return "Graduate degree"

  def urban(value):
    if value == 1:
      return "Rural (country side)"
    elif value == 2:
      return "Subrban"
    elif value == 3:
      return "Urban (town, city)"

  def gender(value):
    if value == 1:
      return "Male"
    elif value == 2:
      return "Female"
    elif value == 3:
      return "Other"

  def married(value):
    if value == 1:
      return "Never married"
    elif value == 2:
      return "Currently married"
    elif value == 3:
      return "Previously married"

  def age(value):
    if value == 1:
      return "Below 10"
    elif value == 2:
      return "10-16"
    elif value == 3:
      return "17-21"
    elif value == 4:
      return "22-35"
    elif value == 5:
      return "36-48"
    elif value == 6:
      return "Above 49"


####################################################################################################################
if __name__ == "__main__":
  app.run(host='0.0.0.0', debug=True)
