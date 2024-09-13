from tabulate import tabulate
from database_config.db_settings import execute_query
from queries.admin.admin_project_statistic_operations import get_all_projects


def get_data_for_season():
    season_name = input("Enter season name (ex: Season 1): ").strip().title()
    start_date = input("Enter start date (ex: 2025-01-01): ").strip()
    end_date = input("Enter end date (ex: 2025-12-31): ").strip()
    return season_name, start_date, end_date


def start_new_season():
    """
    This function is used to start a new season.
    """
    name, start_date, end_date = get_data_for_season()

    deactivate_query = """
    UPDATE seasons
    SET is_active = FALSE
    WHERE is_active = TRUE;
    """
    execute_query(deactivate_query)

    insert_query = f"""
    INSERT INTO seasons (name, is_active, start_date, end_date)
    VALUES ('{name}', TRUE, '{start_date}', '{end_date}');
    """
    execute_query(insert_query)
    print(f"New season '{name}' started successfully.")


def show_active_seasons():
    query = """ SELECT * FROM seasons WHERE is_active = TRUE; """
    result = execute_query(query, fetch='all')
    if result and isinstance(result, (tuple, list)) and len(result) > 0:
        headers = ["ID", "Season Name", "Start", "End"]
        print(tabulate(result, headers=headers, tablefmt="fancy_grid"))
        return result
    else:
        print("No active seasons found, sorry.")
        return None


def end_season():
    print("Currently active season: ")
    show_active_seasons()
    admin_choice = input("Would you like to end the season? (y/n): ").strip().lower()
    if admin_choice == 'y':
        query = """UPDATE seasons SET is_active = 0"""
        execute_query(query)
        print("Season ended successfully.")
    else:
        print("Season not ended.")


def accept_projects():
    get_all_projects()
    project_title = input("Enter project title to accept it: ").strip().title()
    query = f"""UPDATE projects SET statuses_id = 2 WHERE title = '{project_title}';"""
    execute_query(query)
    if query:
        print("Project accepted successfully.")
    else:
        print("You have entered an invalid title. Try again later")


def reject_projects():
    get_all_projects()
    project_title = input("Enter project title to accept it: ").strip().title()
    query = f"""UPDATE projects SET statuses_id = 3 WHERE title = '{project_title}';"""
    execute_query(query)
    if query:
        print("Project accepted successfully.")
    else:
        print("You have entered an invalid title. Try again later")


def show_all_seasons():
    query = """ SELECT * FROM seasons WHERE is_active = TRUE; """
    result = execute_query(query, fetch='all')
    if result and isinstance(result, (tuple, list)) and len(result) > 0:
        headers = ["ID", "Season Name", "Start", "End"]
        print("All seasons:\n")
        print(tabulate(result, headers=headers, tablefmt="fancy_grid"))
        return result
    else:
        print("No seasons found yet, sorry.")
        return None

