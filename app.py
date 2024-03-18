from flask import Flask, render_template, request, jsonify, url_for, redirect, session, g
from flask_sqlalchemy import SQLAlchemy
import bcrypt
import pickle
import numpy as np
from sqlalchemy import desc
from flask_socketio import join_room, leave_room, send, SocketIO
import json

# from viz import visualize_male_female_ratio_in_hero
# import matplotlib.pyplot as plt



app = Flask(__name__)
socketio = SocketIO(app)

####################################################################################################################
# Importing ml models

with open('model_d.pkl', 'rb') as model_file:
  loaded_objects_d = pickle.load(model_file)

model_d = loaded_objects_d["model"]
scaler_d = loaded_objects_d["scaler"]

with open('model_a.pkl', 'rb') as model_file:
  loaded_objects_a = pickle.load(model_file)

model_a = loaded_objects_a["model"]
scaler_a = loaded_objects_a["scaler"]

with open('model_s.pkl', 'rb') as model_file:
  loaded_objects_s = pickle.load(model_file)

model_s = loaded_objects_s["model"]
scaler_s = loaded_objects_s["scaler"]


####################################################################################################################
rooms = {}
# Function to save the rooms dictionary to a JSON file
def save_rooms(rooms):
    with open("rooms.json", "w") as file:
        json.dump(rooms, file)

# Function to load the rooms dictionary from a JSON file
def load_rooms():
    try:
        with open("rooms.json", "r") as file:
            return json.load(file)
    except FileNotFoundError:
        # Return an empty dictionary if the file doesn't exist
        return {}

# Load the rooms dictionary from file when the program starts
rooms = load_rooms()

####################################################################################################################
# Making database and functions to store user data 



app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database.db'

db = SQLAlchemy(app)
app.secret_key = 'secret_key'


# Hero table
class userHero(db.Model):
  # info column
  id = db.Column(db.Integer, primary_key=True)
  name = db.Column(db.String(100), nullable=False)
  email = db.Column(db.String(100), unique = True, nullable=False)
  password = db.Column(db.String(100), nullable=False)
  #question and answer columns
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

  d_result = db.Column(db.String(100))
  a_result = db.Column(db.String(100))
  s_result = db.Column(db.String(100))
  suicidal_result = db.Column(db.String(100))

  room_id = db.Column(db.String(100))

  # suicidal_tendency_count = db.Column(db.Integer, default = 0)

  # saving hero's detail in table
  def __init__(self, name, email, password):
    self.name = name
    self.email = email
    self.password = bcrypt.hashpw(password.encode('utf-8'),
                                  bcrypt.gensalt()).decode('utf-8')

  # matching and checking password
  def check_password(self, password):
    return bcrypt.checkpw(password.encode('utf-8'),
                          self.password.encode('utf-8'))

  # saving hero's set 1 questions (DASS) in table
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

  # saving hero's set 2 questions (TIPI) in table
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

  # saving hero's set 3 questions (personal info) in table
  def update_answers2(self, education, urban, gender, married, familysize,
                      age_group, about):
    self.education = education
    self.urban = urban
    self.gender = gender
    self.married = married
    self.familysize = familysize
    self.age_group = age_group
    self.about = about

  # saving hero's results got from the ml model
  def update_results(self, d_result, a_result, s_result, suicidal_result):
    self.d_result = d_result
    self.a_result = a_result
    self.s_result = s_result
    self.suicidal_result = suicidal_result

  # saving hero's room id
  def update_room_id(self, room_id):
    self.room_id = room_id

  # updating suicidal_count
  # def update_suicidal_tendency_count(self, message):
  #   message_vectorized = vectorizer.transform([message])
  #   pred = suicidal_model.predict(message_vectorized)

  #   if pred == "suicidal":
  #     self.suicidal_tendency_count += 1

  #   db.session.commit()


###############################################################

# Counselor's table
class userCounselor(db.Model):
  id = db.Column(db.Integer, primary_key=True)
  email = db.Column(db.String(100), unique = True, nullable=False)
  name = db.Column(db.String(100), nullable=False)
  password = db.Column(db.String(100), nullable=False)
  gender = db.Column(db.String(100), nullable=False)
  age = db.Column(db.String(100), nullable=False)
  occupation = db.Column(db.String(100), nullable=False)
  time = db.Column(db.String(100), nullable=False)
  phone_no = db.Column(db.String(100), nullable=False)
  about = db.Column(db.String(1000), nullable=False)

  # saving counselor's info in table
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

  # matching and checking password
  def check_password(self, password):
    return bcrypt.checkpw(password.encode('utf-8'),
                          self.password.encode('utf-8'))

###############################################################
# making connection table for all connected counselors and heroes

class connection(db.Model):
  id = db.Column(db.Integer, primary_key=True)
  counselor_email = db.Column(db.String(100), nullable=False)
  hero_email = db.Column(db.String(100), nullable=False)

  def __init__(self, counselor_email, hero_email):
    self.counselor_email = counselor_email
    self.hero_email = hero_email

###############################################################
# creating i.e commiting the db
with app.app_context():
  db.create_all()


####################################################################################################################

# Creating all the routes


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

# hero registeration
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

# hero login
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

# counselor registeration
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

# counselor login 
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

###############################################################

# landing page
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


# set 1 question (DASS)
@app.route("/questions", methods=['GET', 'POST'])
def questions():
  user = None
  user1 = None
  # checking for the users, if logged in any
  if 'email' in session:
    user = userHero.query.filter_by(email=session['email']).first()
    user1 = userCounselor.query.filter_by(email=session['email']).first()

  if user:
    if request.method == 'POST':
      # getting the answers from the form
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

      # updating the answers in the database
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

      return redirect(url_for('result'))
  else:
    return render_template('counselor_access_denied_questions.html',
                           user=user1)
  return render_template('questions2.html', user=user)


@app.route("/result", methods=['post', 'get'])
def result():
  user = None
  user1 = None
  if 'email' in session:
    user = userHero.query.filter_by(email=session['email']).first()
    user1 = userCounselor.query.filter_by(email=session['email']).first()

  if user:
    details_d = [user.Q3A, user.Q5A, user.Q10A, user.Q13A, user.Q16A, user.Q17A, user.Q21A, user.Q24A, user.Q26A, user.Q31A, user.Q34A, user.Q37A, user.Q38A, user.Q42A, user.TIPI1, user.TIPI2, user.TIPI3, user.TIPI4, user.TIPI5, user.TIPI6, user.TIPI7, user.TIPI8, user.TIPI9, user.TIPI10, user.education, user.urban, user.gender, user.married, user.familysize, user.age_group]

    details_a = [user.Q2A, user.Q4A, user.Q7A, user.Q9A, user.Q15A, user.Q19A, user.Q20A, user.Q23A, user.Q25A, user.Q28A, user.Q30A, user.Q36A, user.Q40A, user.Q41A, user.TIPI1, user.TIPI2, user.TIPI3, user.TIPI4, user.TIPI5, user.TIPI6, user.TIPI7, user.TIPI8, user.TIPI9, user.TIPI10, user.education, user.urban, user.gender, user.married, user.familysize, user.age_group]

    details_s = [user.Q1A, user.Q6A, user.Q8A, user.Q11A, user.Q12A, user.Q14A, user.Q18A, user.Q22A, user.Q27A, user.Q29A, user.Q32A, user.Q33A, user.Q35A, user.Q39A, user.Q41A, user.TIPI1, user.TIPI2, user.TIPI3, user.TIPI4, user.TIPI5, user.TIPI6, user.TIPI7, user.TIPI8, user.TIPI9, user.TIPI10, user.education, user.urban, user.gender, user.married, user.familysize, user.age_group]

    details_d = np.array(details_d).reshape(1, -1)
    details_a = np.array(details_a).reshape(1, -1)
    details_s = np.array(details_s).reshape(1, -1)

    details_d = scaler_d.transform(details_d)
    details_a = scaler_a.transform(details_a)
    details_s = scaler_s.transform(details_s)

    d_result = model_d.predict(details_d)[0]
    a_result = model_a.predict(details_a)[0]
    s_result = model_s.predict(details_s)[0]
    suicidal_result = "coming soon"

    user.update_results(d_result, a_result, s_result, suicidal_result)

    db.session.commit()
    
    return render_template('result.html', user=user)
  else:
    return render_template('home.html', user=user1)


@app.route("/select_counselor")
def select_counselor():

  user = None
  user1 = None

  unique_genders = [
      gender[0]
      for gender in db.session.query(userCounselor.gender).distinct().all()
  ]
  unique_ages = [
      age[0] for age in db.session.query(userCounselor.age).distinct().all()
  ]
  unique_occupations = [
      occupation[0] for occupation in db.session.query(
          userCounselor.occupation).distinct().all()
  ]
  unique_times = [
      time[0]
      for time in db.session.query(userCounselor.time).distinct().all()
  ]

  if 'email' in session:
    user = userHero.query.filter_by(email=session['email']).first()
    user1 = userCounselor.query.filter_by(email=session['email']).first()

  if user:
    return render_template('select_counselor.html',
                           user=user,
                           genders=unique_genders,
                           ages=unique_ages,
                           occupations=unique_occupations,
                           times=unique_times)
  else:
    return render_template('home.html', user=user1)


@app.route("/available_counselors", methods=['post', 'get'])
def available_counselors():
  user = None
  user1 = None

  gender = request.form['gender']
  occupation = request.form['occupation']
  time = request.form['time']
  age = request.form['age']

  counselors = userCounselor.query.filter_by(gender=gender,
                                             occupation=occupation,
                                             age=age,
                                             time=time).all()

  if 'email' in session:
    user = userHero.query.filter_by(email=session['email']).first()
    user1 = userCounselor.query.filter_by(email=session['email']).first()

  if user:
    return render_template('available_counselors.html',
                           user=user,
                           counselors=counselors)
  else:
    return render_template('home.html', user=user1)


@app.route("/counselor/profile", methods=['post', 'get'])
def counselor_page():
  user = None
  user1 = None

  counselor_email = request.form.get('email', '')
  counselor = userCounselor.query.filter_by(email=counselor_email).first()

  email_connect = request.form.get('email_connect')

  # create = request.form.get('create')

  if 'email' in session:
    user = userHero.query.filter_by(email=session['email']).first()
    user1 = userCounselor.query.filter_by(email=session['email']).first()

  if email_connect:
    new_connection = connection(counselor_email = email_connect, hero_email = session['email'])
    room = user.name + counselor.name
    user.update_room_id(room)
    rooms[room] = {"members": 0, "messages": []}
    session['name'] = user.name
    db.session.add(new_connection)
    db.session.commit()
    return render_template('counselor_page.html', user=user, counselor=counselor, Connected="Connected")

  if user:
    return render_template('counselor_page.html',
                           user=user,
                           counselor=counselor)  

  else:
    return redirect(url_for('landing_page'))


@app.route("/profile")
def user_profile():
  user = None
  user1 = None
  if 'email' in session:
    user = userHero.query.filter_by(email=session['email']).first()
    user1 = userCounselor.query.filter_by(email=session['email']).first()

  # to find counselors name for the hero's page
  connection_row = connection.query.filter_by(hero_email=session['email']).order_by(desc('id')).first()
  counselor_email = connection_row.counselor_email if connection_row else None
  counselor = userCounselor.query.filter_by(email=counselor_email).first()

  # to find the heroes details for the counselors page
  connection_rows = connection.query.filter_by(counselor_email=session['email']).all()
  hero_emails = [row.hero_email for row in connection_rows]
  heroes_data = []

  for email in set(hero_emails):
      hero = userHero.query.filter_by(email=email).first()
      if hero:
          session["room"] = hero.room_id
          heroes_data.append((hero.name, hero.room_id))

  if user:
    session["room"] = user.room_id
    session["name"] = user.name
    return render_template('profile_hero.html',
                           user=user,
                           dass=convert.dass,
                           tipi=convert.tipi,
                           edu=convert.edu,
                           urban=convert.urban,
                           gender=convert.gender,
                           married=convert.married,
                           age=convert.age, counselor = counselor)
  elif user1:
    session["name"] = user1.name
    return render_template('profile_counselor.html', user=user1, heroes=heroes_data)

  else:
    return redirect(url_for('landing_page')) 

    
#####################################

@app.route("/chat", methods=['post', 'get'])
def chat():
  user = None
  user1 = None

  if 'email' in session:
    user = userHero.query.filter_by(email=session['email']).first()
    user1 = userCounselor.query.filter_by(email=session['email']).first()

  if user:
    room = request.form['room_id']
    session["room"] = room
    session["name"] = user.name
    if room is None or session.get("name") is None or room not in rooms:
      return redirect(url_for("user_profile"))
  
    return render_template("chat.html",
                           user = user,
                           code=room,
                           messages=rooms[room]["messages"])
  elif user1:
    room = request.form['room_id']
    session["room"] = room
    session["name"] = user1.name
    if room is None or session.get("name") is None or room not in rooms:
      return redirect(url_for("user_profile"))

    return render_template("chat.html",
                           user = user1,
                           code=room,
                           messages=rooms[room]["messages"])
  else:
    return redirect(url_for('landing_page'))

@socketio.on("message")
def message(data):
  room = session.get("room")
  if room not in rooms:
    return

  # user = None
  # user1 = None

  # if 'email' in session:
  #   user = userHero.query.filter_by(email=session['email']).first()
    # user1 = userCounselor.query.filter_by(email=session['email']).first()

  content = {"name": session.get("name"), "message": data["data"]}

  # if user:
  #   user.update_suicidal_tendency_count(content["message"])


  send(content, to=room)
  rooms[room]["messages"].append(content)
  save_rooms(rooms)
  print(f"{session.get('name')} said: {data['data']}")


@socketio.on("connect")
def connect(auth):
  room = session.get("room")
  name = session.get("name")
  if not room or not name:
    return
  if room not in rooms:
    leave_room(room)
    return

  join_room(room)
  send({"name": name, "message": "has joined the chat"}, to=room)
  rooms[room]["members"] += 1
  print(f"{name} joined room {room}")


@socketio.on("disconnect")
def disconnect():
  room = session.get("room")
  name = session.get("name")
  leave_room(room)

  if room in rooms:
    rooms[room]["members"] -= 1
    if rooms[room]["members"] <= 0:
      pass

  send({"name": name, "message": "has left the chat"}, to=room)
  print(f"{name} has left the chat")


################################### 


####################################################################################################################


@app.route("/api/trial", methods = ['GET', 'POST'])
def trial():
  user = None
  user1 = None
  if 'email' in session:
    user = userHero.query.filter_by(email=session['email']).first()
    user1 = userCounselor.query.filter_by(email=session['email']).first()

  # if user:
  #   return render_template('counselor_page.html', user=user)
  # elif user1:
  #   return render_template('home.html', user=user1)
  # else:
  #   return render_template('counselor_page.html', counselor=user, user=user1)
  return jsonify(rooms)


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

@app.route("/api/connection_table", methods=['GET', 'POST'])
def show_table2():
  user_data = connection.query.all()
  all_rows = []
  for row in user_data:
    row_dict = row.__dict__
    row_dict.pop('_sa_instance_state', None)
    all_rows.append(row_dict)

  return jsonify(all_rows)


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
  socketio.run(app, host='0.0.0.0', debug=True)