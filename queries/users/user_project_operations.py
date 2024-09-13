from datetime import datetime
from tabulate import tabulate
from database_config.db_settings import execute_query


def show_regions():
    query = """
    SELECT regions_id, name FROM regions
    """
    result = execute_query(query, fetch="all")
    headers = ["ID", "Region Name"]
    print(tabulate(result, headers=headers, tablefmt="github"))
    return result


def get_regions():
    regions = show_regions()
    region_ids = []

    for row in regions:
        region_ids.append(str(row[0]))

    chosen_region = input("Please enter an ID of the region to choose: ").strip()

    if chosen_region in region_ids:
        return int(chosen_region)
    else:
        print("Invalid region ID, try again")
        return get_regions()


def get_districts(region_id):
    query = f"""
        SELECT districts_id, name
        FROM districts
        WHERE regions_id = {region_id}
        """
    result = execute_query(query, fetch="all")
    headers = ["District ID", "District Name"]
    print(tabulate(result, headers=headers, tablefmt="github"))
    chosen_district = input("Please enter an ID of the district to choose: ").strip()

    district_ids = []
    for row in result:
        district_ids.append(str(row[0]))

    if chosen_district in district_ids:
        return int(chosen_district)
    else:
        print("Invalid district ID, try again")
        return get_districts(region_id)


def get_pending_status_id():
    """
    This function retrieves the 'statuses_id' for the status 'pending'
    """
    query = """
    SELECT statuses_id FROM statuses WHERE status_name = 'pending'
    """
    result = execute_query(query, fetch="one")
    if result:
        return result[0]
    else:
        print("'pending' status not found in the statuses table.")
        return None


def show_categories():
    query = """
    SELECT categories_id, name
    FROM categories
    """
    result = execute_query(query, fetch="all")
    headers = ["Category ID", "Category Name"]
    print(tabulate(result, headers=headers, tablefmt="github"))
    return result


def get_category_id_by_name():
    categories = show_categories()
    categories_ids = []

    for row in categories:
        categories_ids.append(str(row[0]))

    chosen_category = input("Please enter an ID of the category to choose: ").strip()
    if chosen_category in categories_ids:
        return int(chosen_category)
    else:
        print("Invalid category ID, try again")
        return get_category_id_by_name()


def get_logged_in_user_id():
    query = """
    SELECT users_id FROM users WHERE is_login = TRUE
    """
    result = execute_query(query, fetch="one")
    return result[0] if result else None


def get_user_id_by_phone(phone_number):
    query = """
    SELECT users_id FROM users WHERE phone_number = %s
    """
    result = execute_query(query, (phone_number,), fetch="one")
    return result[0] if result else None


def get_project_data():
    try:
        project_title = input("Project Title: ").strip().title()
        project_description = input("Project Description: ").strip().title()
        regions = get_regions()
        districts = get_districts(region_id=get_regions())
        community_name = input("Community ('Mahalla') Name (ex: 'Furqat' mahallasi): ").strip()
        estimated_cost = input("Estimated Cost in sums (ex: 100000000): ").strip()
        submitted_at = datetime.now()

        return project_title, project_description, regions, districts, community_name, estimated_cost, submitted_at
    except Exception as e:
        print(e)


def check_user_submitted_project(user_id):
    query = """
    SELECT 1 FROM projects WHERE users_id = %s
    """
    result = execute_query(query, (user_id,), fetch="one")
    return result is not None


def insert_project_data():
    phone_number = input("Please enter your phone number: ").strip()
    current_user_id = get_user_id_by_phone(phone_number)

    if current_user_id is None:
        print("User not found. Please check the phone number.")
        return

    if check_user_submitted_project(current_user_id):
        print("Sorry, one user can submit only one project. You already have a submitted one.")
        return

    category_id = get_category_id_by_name()
    project_data = get_project_data()
    pending_status_id = get_pending_status_id()

    query = """
    INSERT INTO projects 
    (users_id, categories_id, title, description, regions_id, districts_id, community_name, 
    estimated_cost, submitted_at, statuses_id) 
    VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
    """

    data_to_insert = (current_user_id, category_id, *project_data, pending_status_id)
    execute_query(query, data_to_insert)
    print("Your project data has been submitted successfully!")


def show_user_project():
    phone_number = input("Please enter your phone number: ").strip()
    current_user_id = get_user_id_by_phone(phone_number)

    if current_user_id is None:
        print("User not found. Please check the phone number.")
        return

    query = """
        SELECT p.projects_id, u.full_name AS user_name, c.name AS category_name,
            p.title, p.description, r.name AS region_name, d.name AS district_name,
            p.community_name, p.estimated_cost, p.submitted_at, s.status_name
        FROM projects p
        JOIN users u ON p.users_id = u.users_id
        JOIN categories c ON p.categories_id = c.categories_id
        JOIN regions r ON p.regions_id = r.regions_id
        JOIN districts d ON p.districts_id = d.districts_id
        JOIN statuses s ON p.statuses_id = s.statuses_id
        WHERE p.users_id = %s;
    """

    result = execute_query(query, (current_user_id,), fetch='all')
    headers = ["Project ID", "User Name", "Category Name", "Title", "Description", "Region Name", "District Name",
               "Community Name", "Estimated Cost", "Submitted At", "Status"]
    print(tabulate(result, headers=headers, tablefmt="fancy_grid"))