from database_config.models import create_table
from queries.admin.admin_project_statistic_operations import get_all_projects, get_total_number_of_projects, \
    get_projects_per_region, get_projects_above_budget, get_average_budget, get_total_budget, search_project_by_letter, \
    show_all_categories
from queries.admin.admin_season_operations import show_active_seasons, end_season, reject_projects, accept_projects, \
    start_new_season, show_all_seasons
from queries.admin.admin_table_operations import add_categories, update_category_name, delete_category
from queries.admin.admin_user_statistic_operations import get_all_users, get_one_user, get_all_phone_numbers, \
    get_total_number_of_users, get_all_user_names, get_only_active_users, search_user_by_letter
from queries.admin.admin_voting_statistic_operations import show_all_voted_projects, show_all_non_voted_projects, \
    get_winners
from queries.table_data.insert_data import add_regions_data, add_districts_data, add_status_data
from queries.users.user_authorization import insert_registered_data
from queries.users.user_data_operations import change_user_login, change_user_password, change_user_full_name
from queries.users.user_project_operations import insert_project_data, show_user_project
from queries.users.user_voting_operations import count_votes_per_project, vote_for_project
from utils.checkdata import check_user, check_admin


def show_project_related_menu() -> None:
    """
    This function is used to show the project related menu.
    :return: None
    """
    text = input("""
1. Submit a project.
2. See my project.
3. Go to back.
Choose an option: """)
    if text == '1':
        insert_project_data()
    elif text == '2':
        show_user_project()
    elif text == '3':
        show_user_main_menu()
    else:
        print('Invalid option!')
    show_project_related_menu()


def show_voting_related_menu() -> None:
    """
    This function is used to show the voting related menu.
    :return: None
    """
    text = input("""
1. Vote for a project.
2. See all votes.
3. Go to back.
Choose an option: """)
    if text == '1':
        vote_for_project()
    elif text == '2':
        count_votes_per_project()
    elif text == '3':
        show_user_main_menu()
    else:
        print('Invalid option!')
    show_voting_related_menu()


def show_personal_related_menu() -> None:
    """
    This function is used to show the personal related menu.
    :return:
    """
    text = input("""
1. Update my login.
2. Update my password.
3. Update my full name.
4. Go to back.
Choose an option: """)
    if text == '1':
        change_user_login()
    elif text == '2':
        change_user_password()
    elif text == '3':
        change_user_full_name()
    elif text == '4':
        show_user_main_menu()
    else:
        print('Invalid option!')
    show_personal_related_menu()


def show_user_main_menu() -> None:
    """
    This function is used to show the user main menu.
    :return: None
    """
    text = input("""
1. Project related.
2. Voting related.
3. Personal data related.
4. Go to main menu.
Choose an option: """)
    if text == '1':
        show_project_related_menu()
    elif text == '2':
        show_voting_related_menu()
    elif text == '3':
        show_personal_related_menu()
    elif text == '4':
        show_main_menu()
    else:
        print('Invalid option!')
    show_user_main_menu()


# Admin menu # Admin menu # Admin menu # Admin menu
def show_season_related_menu() -> None:
    """
    This function is used to show the season related menu.
    :return: None
    """
    text = input("""
1. Start a new season.
2. End a season.
3. Accept a project.
4. Reject a project.
5. Go to back.
Choose an option: """)
    if text == '1':
        start_new_season()
    elif text == '2':
        end_season()
    elif text == '3':
        accept_projects()
    elif text == '4':
        reject_projects()
    elif text == '5':
        show_admin_main_menu()
    else:
        print('Invalid option!')
    show_season_related_menu()


def show_user_statistics_related_menu() -> None:
    """
    This function is used to show the user statistics related menu.
    :return: None
    """
    text = input("""
1. See full user data.
2. See one user data.
3. Check number of users.
4. See only phone numbers.
5. See only names.
6. Search user by a letter.
7. See all active users.
8. Go to back.
Choose an option: """)
    if text == '1':
        get_all_users()
    elif text == '2':
        get_one_user()
    elif text == '3':
        get_total_number_of_users()
    elif text == '4':
        get_all_phone_numbers()
    elif text == '5':
        get_all_user_names()
    elif text == '6':
        search_user_by_letter()
    elif text == '7':
        get_only_active_users()
    elif text == '8':
        show_statistics_related_menu()
    else:
        print('Invalid option!')
    show_user_statistics_related_menu()


def show_project_statistics_related_menu() -> None:
    """
    This function is used to show the project statistics related menu.
    :return: None
    """
    text = input("""
1. See all projects.
2. Check total number of projects.
3. Project numbers per region.
4. Average budget of projects.
5. Projects above certain budget.
6. Total budget of projects.
7. Search project by a letter.
8. Go to back.
Choose an option: """)

    if text == '1':
        get_all_projects()
    elif text == '2':
        get_total_number_of_projects()
    elif text == '3':
        get_projects_per_region()
    elif text == '4':
        get_average_budget()
    elif text == '5':
        get_projects_above_budget()
    elif text == '6':
        get_total_budget()
    elif text == '7':
        search_project_by_letter()
    elif text == '8':
        show_admin_main_menu()
    else:
        print('Invalid option!')
    show_project_statistics_related_menu()


def show_statistics_related_menu() -> None:
    """
    This function is used to show the statistics related menu.
    :return: None
    """
    text = input("""
1. User statistics.
2. Project statistics.
3. See all categories.
4. See all voted projects.
5. See all non-voted projects.
6. See winners.
7. See all seasons.
8. Go to back.
Choose an option: """)
    if text == '1':
        show_user_statistics_related_menu()
    elif text == '2':
        show_project_statistics_related_menu()
    elif text == '3':
        show_all_categories()
    elif text == '4':
        show_all_voted_projects()
    elif text == '5':
        show_all_non_voted_projects()
    elif text == '6':
        get_winners()
    elif text == '7':
        show_all_seasons()
    elif text == '8':
        show_admin_main_menu()
    else:
        print('Invalid option!')
    show_statistics_related_menu()


def show_table_related_menu() -> None:
    """
    This function is used to show the table related menu.
    :return:
    """
    text = input("""
1. Add categories.
2. Update a category.
3. Delete a category.
4. Go to back.
""")
    if text == '1':
        add_categories()
    elif text == '2':
        update_category_name()
    elif text == '3':
        delete_category()
    elif text == '4':
        show_admin_main_menu()
    else:
        print('Invalid option!')
    show_table_related_menu()


def show_admin_main_menu() -> None:
    """
    This function is used to show the admin main menu.
    :return: None
    """
    text = input("""
1. Statistics related.
2. Table related.
3. Season related.
4. Go to main menu.
Choose an option: """)
    if text == '1':
        show_statistics_related_menu()
    elif text == '2':
        show_table_related_menu()
    elif text == '3':
        show_season_related_menu()
    elif text == '4':
        show_main_menu()
    else:
        print('Invalid option!')
    show_admin_main_menu()


def show_main_menu() -> None:
    """
    This function displays the main menu of the 'Open Budget' system, allowing users to register, log in, or exit.
    """
    print("\nWelcome to 'Open Budget' system!\n")
    text = input("""
1. Register (for users only).
2. Login.
3. Exit.

Choose an option: """)

    if text == "1":
        insert_registered_data()
    elif text == "2":
        login = input("Enter your login: ").strip()
        password = input("Enter your password: ").strip()
        if check_user(login, password):
            print(f"Welcome back, {login}!\n")
            return show_user_main_menu()
        elif check_admin(login, password):
            print(f"Welcome back, {login}!\n")
            return show_admin_main_menu()
        else:
            print("Invalid login or password!")
            show_main_menu()
    elif text == "3":
        print("Thank you for using our system!")
    else:
        print("Invalid option!")
    show_main_menu()


if __name__ == '__main__':
    create_table()
    add_regions_data()
    add_districts_data()
    add_status_data()
    show_main_menu()
