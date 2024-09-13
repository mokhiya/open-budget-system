from tabulate import tabulate
from database_config.db_settings import execute_query
from queries.admin.admin_season_operations import show_active_seasons
from queries.users.user_project_operations import get_user_id_by_phone


def get_user_phone() -> tuple:
    """
    This function gets the user phone number
    :returns Tuple
    """
    phone_number = input("Please, enter a phone number you used for registration: ").strip()
    result = get_user_id_by_phone(phone_number)
    if result:
        return result
    else:
        print("Invalid phone number.")
        return get_user_phone()


def get_project_title() -> tuple:
    """
    This function gets the project title
    :returns Tuple
    """
    query = """
    SELECT p.projects_id, p.title,
           ROW_NUMBER() OVER(ORDER BY p.submitted_at) AS temp_id
    FROM projects p;
    """
    result = execute_query(query, fetch='all')
    headers = ["Project UUID", "Title", "Temporary ID"]
    print(tabulate(result, headers=headers))
    return result


def get_project_id():
    projects = get_project_title()

    while True:
        try:
            temp_id = int(input("Please, enter a project ID (temporary number): "))
            if 1 <= temp_id <= len(projects):
                selected_project = projects[temp_id - 1]
                real_project_id = selected_project[0]
                print(f"Selected Project UUID: {real_project_id}")
                return real_project_id
            else:
                print(f"Invalid project ID. Please enter a number between 1 and {len(projects)}.")
        except ValueError:
            print("Invalid input. Please enter a valid number.")


def get_season_id() -> int | None:
    """
    This function gets the season ID
    :return: integer or None
    """
    seasons = show_active_seasons()
    if seasons is None:
        return None

    valid_season_ids = {season[0] for season in seasons}

    while True:
        try:
            season_id = int(input("Please, enter a season ID: "))
            if season_id in valid_season_ids:
                print(f"Selected Season ID: {season_id}")
                return season_id
            else:
                print(f"Invalid season ID. Please enter a valid ID from the list.")
        except ValueError:
            print("Invalid input. Please enter a valid number.")


def vote_for_project():
    """
    This functions used to vote for project
    """
    project_id = get_project_id()
    season_id = get_season_id()
    user_id = get_user_phone()

    if project_id is None or season_id is None:
        return
    # Checking if the user has already voted
    query_check = """ SELECT COUNT(*) FROM voting WHERE users_id = %s AND seasons_id = %s;"""
    result = execute_query(query_check, (user_id, season_id), fetch='one')

    if result and result[0] > 0:
        print("You have already voted for a project in this season.")
        return

    # Inserting the vote if the user has not voted yet
    query_insert = """ INSERT INTO voting (projects_id, seasons_id, users_id) VALUES (%s, %s, %s); """
    execute_query(query_insert, (project_id, season_id, user_id))
    print("You have voted successfully!")


def count_votes_per_project():
    """
    This function counts the number of votes per project
    """
    query = """
        SELECT p.projects_id, p.title, COUNT(v.voting_id) AS vote_count
        FROM projects p
        LEFT JOIN voting v ON p.projects_id = v.projects_id
        GROUP BY p.projects_id, p.title;
    """
    result = execute_query(query, fetch='all')
    headers = ["Project ID", "Title", "Vote Count"]
    print(tabulate(result, headers=headers, tablefmt="fancy_grid"))
