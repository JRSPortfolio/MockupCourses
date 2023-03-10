from typing import List
from data.models import Testimonial

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
    