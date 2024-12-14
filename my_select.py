from sqlalchemy import select, func
from sqlalchemy.orm import Session
from db.models import Group, Student, Subject, Grade
from db.config import session


def format_results(results):
    """
    Форматує результати запиту у зручний для читання формат.
    """
    if not results:
        return "Немає даних для відображення."

    if isinstance(results, list):
        # Форматуємо список результатів
        formatted = "\n".join(
            f"{', '.join(map(str, row))}"
            for row in results
        )
    else:
        # Форматуємо окреме значення
        formatted = str(results)

    return formatted


def select_1(session: Session):
    # Знайти 5 студентів із найбільшим середнім балом з усіх предметів.
    print("\n" f"Select 1: \n{"-" * 40}")
    stmt = (
        select(Student.name, func.avg(Grade.grade).label("avg_grade"))
        .join(Grade, Student.id == Grade.student_id)
        .group_by(Student.id)
        .order_by(func.avg(Grade.grade).desc())
        .limit(5)
    )
    result = session.execute(stmt).all()
    return format_results(result)

def select_2(session: Session, subject_id: int):
    # Знайти студента із найвищим середнім балом з певного предмета.
    print("\n" f"Select 2: \n{"-" * 40}")
    stmt = (
        select(Student.name, func.avg(Grade.grade).label("avg_grade"))
        .join(Grade, Student.id == Grade.student_id)
        .filter(Grade.subject_id == subject_id)
        .group_by(Student.id)
        .order_by(func.avg(Grade.grade).desc())
        .limit(1)
    )
    result = session.execute(stmt).first()
    return format_results(result)

def select_3(session: Session, subject_id: int):
    # Знайти середній бал у групах з певного предмета.
    print("\n" f"Select 3: \n{"-" * 40}")
    stmt = (
        select(Group.name, func.avg(Grade.grade).label("avg_grade"))
        .join(Student, Group.id == Student.group_id)
        .join(Grade, Student.id == Grade.student_id)
        .filter(Grade.subject_id == subject_id)
        .group_by(Group.id)
    )
    result = session.execute(stmt).all()
    return format_results(result)

def select_4(session: Session):
    # Знайти середній бал на потоці (по всій таблиці оцінок).
    print("\n" f"Select 4: \n{"-" * 40}")
    stmt = select(func.avg(Grade.grade).label("avg_grade"))
    result = session.execute(stmt).scalar()
    return format_results(result)

def select_5(session: Session, teacher_id: int):
    # Знайти які курси читає певний викладач.
    print("\n" f"Select 5: \n{"-" * 40}")
    stmt = (
        select(Subject.name)
        .filter(Subject.teacher_id == teacher_id)
    )
    result = session.execute(stmt).all()
    return format_results(result)


def select_6(session: Session, group_id: int):
    # Знайти список студентів у певній групі.
    print("\n" f"Select 6: \n{"-" * 40}")
    stmt = (
        select(Student.name)
        .filter(Student.group_id == group_id)
    )
    resultv = session.execute(stmt).all()
    return format_results(resultv)

def select_7(session: Session, group_id: int, subject_id: int):
    # Знайти оцінки студентів у окремій групі з певного предмета.
    print("\n" f"Select 7: \n{"-" * 40}")
    stmt = (
        select(Student.name, Grade.grade)
        .join(Grade, Student.id == Grade.student_id)
        .filter(Student.group_id == group_id, Grade.subject_id == subject_id)
    )
    result = session.execute(stmt).all()
    return format_results(result)

def select_8(session: Session, teacher_id: int):
    # Знайти середній бал, який ставить певний викладач зі своїх предметів.
    print("\n" f"Select 8: \n{"-" * 40}")
    stmt = (
        select(func.avg(Grade.grade).label("avg_grade"))
        .join(Subject, Grade.subject_id == Subject.id)
        .filter(Subject.teacher_id == teacher_id)
    )
    result = session.execute(stmt).scalar()
    return format_results(result)


def select_9(session: Session, student_id: int):
    # Знайти список курсів, які відвідує певний студент.
    print("\n" f"Select 9: \n{"-" * 40}")
    stmt = (
        select(Subject.name)
        .join(Grade, Grade.subject_id == Subject.id)
        .filter(Grade.student_id == student_id)
        .distinct()
    )
    result = session.execute(stmt).all()
    return format_results(result)

def select_10(session: Session, student_id: int, teacher_id: int):
    # Список курсів, які певному студенту читає певний викладач.
    print("\n" f"Select 10: \n{"-" * 40}")
    stmt = (
        select(Subject.name)
        .join(Grade, Grade.subject_id == Subject.id)
        .filter(Grade.student_id == student_id, Subject.teacher_id == teacher_id)
    )
    result = session.execute(stmt).all()
    return format_results(result)


with session as session:
    print(select_1(session))
    print(select_2(session, 1))
    print(select_3(session, 1))
    print(select_4(session))
    print(select_5(session, 1))
    print(select_6(session, 1))
    print(select_7(session, 1, 1))
    print(select_8(session, 1))
    print(select_9(session, 1))
    print(select_10(session, 1, 1))