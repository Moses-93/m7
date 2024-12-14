import my_select
from db.config import session


def main(session):
    with session as session:
        print(my_select.select_1(session))
        print(my_select.select_2(session, 1))
        print(my_select.select_3(session, 1))
        print(my_select.select_4(session))
        print(my_select.select_5(session, 1))
        print(my_select.select_6(session, 1))
        print(my_select.select_7(session, 1, 1))
        print(my_select.select_8(session, 1))
        print(my_select.select_9(session, 1))
        print(my_select.select_10(session, 1, 1))


if __name__ == "__main__":
    main(session)
    