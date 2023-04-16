import os
from sqlalchemy import create_engine, text

db_connection_string = os.environ['DB_CONNECTION_STRING']

engine = create_engine(db_connection_string,
                       connect_args={"ssl": {
                         "ssl_ca": "/etc/ssl/cert.pem"
                       }})



# def load_counselor_from_db(counselor_name):
#   with engine.connect() as conn:
#     result = conn.execute(text(f"SELECT * FROM jobs WHERE counselor_name = {counselor_name}"))
#     rows = result.all()
#     if len(rows) == 0:
#       return None
#     else:
#       return rows[0]._mapping


def add_counselor_to_db(data):
  with engine.connect() as conn:
    query= text("""INSERT INTO counselor_anuyog (counselor_name, name, gender, age, occupation, time_range, about, phone_no, email)
                        VALUES (:counselor_name, :name, :gender, :age, :occupation, :time_range, :about, :phone_no, :email)""")
    params= {'counselor_name': data['counselor_name'],
            'name': data['name'],
            'gender':data['gender'], 
            'age':data['age'], 
            'occupation':data['occupation'], 
            'time_range':data['time_range'], 
            'about':data['about'], 
            'phone_no':data['phone_no'], 
            'email':data['email']
            }
    conn.execute(query, params)


def add_answers_to_db(data):
  with engine.connect() as conn:
    query= text("""INSERT INTO questions_anuyog(question_1,question_2,question_3,question_4,question_5,question_6,question_7,question_8,question_9,question_10,question_11,question_12,question_13,question_14,question_15,question_16,question_17,question_18,question_19,question_20,question_21,question_22,question_23,question_24,question_25,question_26,question_27,question_28,question_29,question_30 )
                        VALUES (:question_1,:question_2,:question_3,:question_4,:question_5,:question_6,:question_7,:question_8,:question_9,:question_10,:question_11,:question_12,:question_13,:question_14,:question_15,:question_16,:question_17,:question_18,:question_19,:question_20,:question_21,:question_22,:question_23,:question_24,:question_25,:question_26,:question_27,:question_28,:question_29,:question_30)""")
    
    params= {'question_1':data['question_1'],
             'question_2':data['question_2'],
             'question_3':data['question_3'],
             'question_4':data['question_4'],
             'question_5':data['question_5'],
             'question_6':data['question_6'],
             'question_7':data['question_7'],
             'question_8':data['question_8'],
             'question_9':data['question_9'],
             'question_10':data['question_10'],
             'question_11':data['question_11'],
             'question_12':data['question_12'],
             'question_13':data['question_13'],
             'question_14':data['question_14'],
             'question_15':data['question_15'],
             'question_16':data['question_16'],
             'question_17':data['question_17'],
             'question_18':data['question_18'],
             'question_19':data['question_19'],
             'question_20':data['question_20'],
             'question_21':data['question_21'],
             'question_22':data['question_22'],
             'question_23':data['question_23'],
             'question_24':data['question_24'],
             'question_25':data['question_25'],
             'question_26':data['question_26'],
             'question_27':data['question_27'],
             'question_28':data['question_28'],
             'question_29':data['question_29'],
             'question_30':data['question_30']}

    conn.execute(query, params)