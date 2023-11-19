from faker import Faker
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from models import Student, Group, Teacher, Subject, StudentSubject
import random

fake = Faker()

engine = create_engine('sqlite:///students.db', echo=True)
Session = sessionmaker(bind=engine)
session = Session()

groups = [Group(name=fake.word()) for _ in range(3)]
session.add_all(groups)
session.commit()

teachers = [Teacher(name=fake.name()) for _ in range(5)]
session.add_all(teachers)
session.commit()

subjects = [Subject(name=fake.word(), teacher=random.choice(teachers)) for _ in range(5)]
session.add_all(subjects)
session.commit()

students = [Student(name=fake.name(), group=random.choice(groups)) for _ in range(30)]
session.add_all(students)
session.commit()

for student in students:
    for subject in subjects:
        score = random.randint(60, 100)  # Випадковий бал
        date_received = fake.date_time_between(start_date="-1y", end_date="now")  # Випадкова дата отримання оцінки
        student_subject = StudentSubject(student=student, subject=subject, score=score, date_received=date_received)
        session.add(student_subject)

session.commit()
session.close()
