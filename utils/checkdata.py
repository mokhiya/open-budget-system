from typing import Tuple, Any

from database_config.db_settings import execute_query

admin_login = "admin"
admin_password = "0000"


def check_admin(login, password) -> bool:
    """
    This function checks if the login and password of admin are correct.
    :param login:
    :param password:
    :return True:
    """
    if login == admin_login and password == admin_password:
        return True
    return False


def get_user_data(login, password):
    """
    This function gets data of user from database.
    :param login:
    :param password:
    """
    query = """
    SELECT users_id, login, password FROM users WHERE login = %s AND password = %s
    """
    result = execute_query(query, (login, password), fetch="one")
    return result


def check_user(login, password) -> tuple | None:
    """
    This function checks if the login and password of user are correct.
    """
    userdata = get_user_data(login, password)
    global current_user_login
    if userdata:
        update_login_status(userdata[0])  # Updating the status to TRUE if credentials match
        current_user_login = login
        return userdata[1], userdata[2]
    else:
        return None


def update_login_status(user_id):
    """
    This function updates the login status of user.
    :param user_id:
    """
    deactivate_query = """
    UPDATE users
    SET is_login = FALSE
    WHERE is_login = TRUE;
    """
    execute_query(deactivate_query)

    activate_query = """
    UPDATE users
    SET is_login = TRUE
    WHERE users_id = %s;
    """
    execute_query(activate_query, (user_id,))
    print(f"User with ID {user_id} logged in successfully.")

