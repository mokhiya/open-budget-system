from database_config.db_settings import execute_query
from utils.checkdata import update_login_status, get_user_data


def check_user(login, password) -> tuple | None:
    """
    This function checks if the login and password of user are correct.
    :return tuple or None
    """
    userdata = get_user_data(login, password)
    global current_user_login
    if userdata:
        update_login_status(userdata[0])  # Updating the status to TRUE if credentials match
        current_user_login = login
        return userdata[1], userdata[2]
    else:
        return None


def change_user_login():
    """
    This function helps user to change his login.
    """
    global current_user_login
    old_login = input("Old login: ").strip()
    new_login = input("New login: ").strip()
    query = """UPDATE users SET login = %s WHERE login = %s"""
    try:
        execute_query(query, [new_login, old_login])
        query_check = "SELECT login FROM users WHERE login = %s"
        result = execute_query(query_check, [new_login], fetch="one")

        if result:
            print("Your login has been changed successfully.")
            current_user_login = new_login
        else:
            print("Update failed. The old login may not exist.")
    except Exception as e:
        print(f"An error occurred: {e}")


def change_user_password():
    """
    This function helps user to change his password.
    """
    global current_user_password
    old_password = input("Old password: ").strip()
    new_password = input("New password: ").strip()

    query = """UPDATE users SET password = %s WHERE password = %s"""

    try:
        execute_query(query, [new_password, old_password])
        query_check = "SELECT password FROM users WHERE password = %s"
        result = execute_query(query_check, [new_password], fetch="one")

        if result:
            print("Your password has been changed successfully.")
            current_user_password = new_password
        else:
            print("Update failed.")
    except Exception as e:
        print(f"An error occurred: {e}")


def change_user_full_name():
    """
    This function changes the full name of the currently logged-in user.
    """
    global current_user_full_name
    old_full_name = input("Previous full name: ").strip()
    new_full_name = input("New full name: ").strip()

    query = """
    UPDATE users 
    SET full_name = %s 
    WHERE full_name = %s AND is_login = TRUE
    """
    try:
        execute_query(query, [new_full_name, old_full_name])

        query_check = """
        SELECT login 
        FROM users 
        WHERE full_name = %s AND is_login = TRUE
        """
        result = execute_query(query_check, [new_full_name], fetch="one")

        if result:
            print(f"Your full name has been changed from {old_full_name}"
                  f" to {new_full_name} successfully.")
            current_user_full_name = new_full_name
        else:
            print("Update failed. Ensure you're logged in with the correct full name.")
    except Exception as e:
        print(f"An error occurred: {e}")

