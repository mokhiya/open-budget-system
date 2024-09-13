import re
from database_config.db_settings import execute_query


def validate_phone_number(phone_number) -> bool:
    """
    This function checks if the phone number is valid.
    :param phone_number:
    :return: bool
    """
    pattern = r'^\+998\d{9}$'
    if re.match(pattern, phone_number):
        return True
    else:
        return False


def register_user():
    """
    This function is used to register a new user
    """
    full_name = input("Enter your full name: ").strip().title()
    while True:
        phone_number = input("Enter your phone number in the following format '+998946718299': ").strip()
        if validate_phone_number(phone_number):
            print("Phone number is valid.")
            break
        else:
            print("Phone number is invalid. Please enter it in the format '+998946718299'.")

    login = input("Think any login: ").strip()
    password = input("Think any password: ").strip()

    return full_name, phone_number, login, password


def insert_registered_data():
    """
    This function is used to insert data about user into the database
    """
    userdata = register_user()

    query = """
    INSERT INTO users (full_name, phone_number, login, password)
    VALUES (%s, %s, %s, %s)
    """
    execute_query(query, userdata)
    print("You have registered successfully!")