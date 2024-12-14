import random
from faker import Faker

from db.config import session, engine
from db.models import Base, Group, Student, Teacher, Subject, Grade


fake = Faker()

Base.metadata.create_all(engine)

def seed_data():

    # Додавання груп
    groups = [Group(name=f"Group {i}") for i in range(1, 4)]
    session.add_all(groups)
    session.commit()
    print("Group table successfully filled in")

    # Додавання викладачів
    teachers = [Teacher(name=fake.name()) for _ in range(4)]
    session.add_all(teachers)
    session.commit()
    print("Teacher table successfully filled in")

    # Додавання предметів
    # Попередньо підготовлений список назв предметів
    subject_names = [
        "Mathematics", "Physics", "Chemistry", "Biology", 
        "History", "Geography", "Literature", "Computer Science"
    ]

    # Генерація предметів
    subjects = [
        Subject(name=random.choice(subject_names), teacher=random.choice(teachers)) 
        for _ in range(6)
    ]
    session.add_all(subjects)
    session.commit()
    print("Subject table successfully filled in")

    # Додавання студентів
    students = [
        Student(name=fake.name(), group=random.choice(groups))
        for _ in range(50)
    ]
    session.add_all(students)
    session.commit()
    print("Student table successfully filled in")

    # Додавання оцінок
    for student in students:
        for subject in subjects:
            for _ in range(random.randint(1, 5)):
                grade = Grade(
                    student=student,
                    subject=subject,
                    grade=random.uniform(2, 5),
                    date=fake.date_this_year()
                )
                session.add(grade)

    session.commit()
    print("Grade table successfully filled in")
    session.close()
    print("All tables successfully filled with data")


if __name__ == "__main__":
    seed_data()
