from tabulate import tabulate
from database_config.db_settings import execute_query


def get_all_users():
    """
    This function gets all users
    :return:
    """
    query = """ SELECT * FROM users; """
    result = execute_query(query, fetch='all')
    headers = ["ID", "Full Name", "Phone number", "Login", "Password", "Status"]
    print(tabulate(result, headers=headers, tablefmt="fancy_grid"))


def get_one_user() -> None:
    """
    This function gets one user data
    :return: None
    """
    user_name = input("Enter user's full name: ").strip().title()
    query = """ SELECT * FROM users WHERE full_name = %s """
    result = execute_query(query, (user_name,), fetch='one')
    if result and isinstance(result, (tuple, list)):
        headers = ["ID", "Full Name", "Phone number", "Login", "Password", "Status"]
        print(tabulate([result], headers=headers, tablefmt="fancy_grid"))
    else:
        print("No user found with that name or invalid result type.")
        return None


def get_total_number_of_users():
    """
    This function gets total number of users
    """
    query = """ SELECT COUNT(users_id) AS Total_Users FROM users; """
    result = execute_query(query, fetch='all')
    headers = ["Total Users"]
    print(tabulate(result, headers=headers, tablefmt="fancy_grid"))


def get_all_phone_numbers():
    """
    This function gets all phone numbers
    """
    query = """ SELECT users_id, phone_number FROM users; """
    result = execute_query(query, fetch='all')
    headers = ["ID", "Phone number"]
    print(tabulate(result, headers=headers, tablefmt="fancy_grid"))


def get_all_user_names():
    """
    This function gets all users names
    """
    query = """ SELECT users_id, full_name FROM users; """
    result = execute_query(query, fetch='all')
    headers = ["ID", "Full Name"]
    print(tabulate(result, headers=headers, tablefmt="fancy_grid"))


def search_user_by_letter():
    missing_letter = input("Enter letter to search for: ").strip().lower()
    query = f"""SELECT * FROM users WHERE full_name like '%{missing_letter}%'"""
    result = execute_query(query, fetch='all')
    if result and isinstance(result, (tuple, list)) and len(result) > 0:
        headers = ["ID", "Full Name", "Phone number", "Login", "Password", "Status"]
        print(tabulate(result, headers=headers, tablefmt="fancy_grid"))
    else:
        print("No user found with that letter or invalid result type.")
        return None


def get_only_active_users():
    """
    This function returns only active users.
    """
    query = """SELECT * FROM users WHERE is_login = 't'; """
    result = execute_query(query, fetch='all')
    if result and isinstance(result, (tuple, list)):
        headers = ["ID", "Full Name", "Phone number", "Login", "Password", "Status"]
        print(tabulate(result, headers=headers, tablefmt="fancy_grid"))
    else:
        print("No user is active right now.")
