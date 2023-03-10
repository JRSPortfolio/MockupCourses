from typing import List
from data.models import Testimonial, Student

def student_count():
    return 2315

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

def every_student():
    return[Student(id = 154,
                   name = 'Jose Lopes',
                   email = 'jl@mail.pt',
                   password = '123456'),
           Student(id = 187,
                   name = 'Albertina Gomes',
                   email = 'ag@mail.pt',
                   password = '123456'),
           Student(id = 198,
                   name = 'Simao Silva',
                   email = 'ss@mail.pt',
                   password = '123456'),
           Student(id = 212,
                   name = 'Beatriz Fialho',
                   email = 'bf@mail.pt',
                   password = '123456')]
    
def get_student_by_id(stud_id: int):
    students = every_student()
    for stud in students:
        if stud.id == stud_id:
            return stud
    return None