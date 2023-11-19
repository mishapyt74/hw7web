from sqlalchemy import create_engine, func
from sqlalchemy.orm import sessionmaker
from models import Student, Group, Teacher, Subject, StudentSubject

engine = create_engine('sqlite:///students.db', echo=True)
Session = sessionmaker(bind=engine)
session = Session()

def select_1():
    top_students = (
        session.query(Student, func.avg(StudentSubject.score).label('average_score'))
        .join(StudentSubject)
        .group_by(Student)
        .order_by(func.avg(StudentSubject.score).desc())
        .limit(5)
        .all()
    )
    return top_students

def select_2(subject_name):
    top_student_in_subject = (
        session.query(Student, func.avg(StudentSubject.score).label('average_score'))
        .join(StudentSubject)
        .join(Subject)
        .filter(Subject.name == subject_name)
        .group_by(Student)
        .order_by(func.avg(StudentSubject.score).desc())
        .first()
    )
    return top_student_in_subject


session.close()
