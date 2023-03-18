from random import randrange
from typing import List
from data.models import Testimonial, Student
from datetime import date
from infrastructure.common import is_valid_email, find_in

def student_count():
    return 2315

_students = []

def create_account(name: str,
                   email: str,
                   password: str,
                   birth_date: date
                   ):
    
    if get_student_by_email(email):
        raise ValueError(f"Utilizador com email {email} já se encontra registado.")
    student = Student(id = randrange(10_000, 100_000),
                      name = name,
                      email = email,
                      password = hash_password(password),
                      birth_date = birth_date)
    _students.append(student)
    return student
    
def get_student_by_email(email: str):
    if not is_valid_email(email):
        raise ValueError(f"Endereço de email {email} inválido")
    return find_in(_students, lambda student: student.email == email)

def authenticate_student_by_email(email, password):
    if student := get_student_by_email(email):
        if hash_password(password) == student.password:
            return student
    return None

def get_testimonials(count: int):
    return[Testimonial(user_id = 239,
                       user_name = 'Saul Goodman',
                       user_occupation = 'CEO & Founder',
                       text = 'Algum texto de testemunho'),
           Testimonial(user_id = 1001,
                       user_name = 'Sara Wilson',
                       user_occupation = 'Designer',
                       text = 'Algum texto de testemunho'),
           Testimonial(user_id = 704,
                       user_name = 'Jena Karlis',
                       user_occupation = 'Store Owner',
                       text = 'Algum texto de testemunho'),
           Testimonial(user_id = 1002,
                       user_name = 'Matt Brandon',
                       user_occupation = 'Freelancer',
                       text = 'Algum texto de testemunho'),
           Testimonial(user_id = 1589,
                       user_name = 'John Larson',
                       user_occupation = 'Entrepreneur',
                       text = 'Algum texto de testemunho')]

def hash_password(password: str):
    return password + '-hashpw'