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