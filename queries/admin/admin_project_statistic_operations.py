from tabulate import tabulate
from database_config.db_settings import execute_query


def get_all_projects():
    query = """
    SELECT p.projects_id, u.full_name AS user_name, c.name AS category_name,
        p.title, p.description, r.name AS region_name, d.name AS district_name,
        p.community_name, p.estimated_cost, p.submitted_at, s.status_name
    FROM projects p
    JOIN users u ON p.users_id = u.users_id
    JOIN categories c ON p.categories_id = c.categories_id
    JOIN regions r ON p.regions_id = r.regions_id
    JOIN districts d ON p.districts_id = d.districts_id
    JOIN statuses s ON p.statuses_id = s.statuses_id;
    """
    result = execute_query(query, fetch='all')
    headers = ["Project ID", "User Name", "Category Name", "Title", "Description", "Region Name", "District Name",
               "Community Name", "Estimated Cost", "Submitted At", "Status"]
    print(tabulate(result, headers=headers, tablefmt="fancy_grid"))


def get_total_number_of_projects():
    query = """ SELECT COUNT(projects_id) AS Total_Projects FROM projects; """
    result = execute_query(query, fetch='all')
    headers = ["Total Projects"]
    print(tabulate(result, headers=headers, tablefmt="fancy_grid"))


def get_projects_per_region():
    query = """
    SELECT r.name AS region_name, COUNT(p.projects_id) AS project_count
    FROM projects p
    JOIN regions r ON p.regions_id = r.regions_id
    GROUP BY r.name;
    """
    result = execute_query(query, fetch='all')
    headers = ["Region Name", "Project Count"]
    print(tabulate(result, headers=headers, tablefmt="fancy_grid"))


def get_average_budget():
    query = """
    SELECT AVG(estimated_cost) AS average_budget
    FROM projects;
    """
    result = execute_query(query, fetch='all')
    headers = ["Average Budget"]
    print(tabulate(result, headers=headers, tablefmt="fancy_grid"))


def get_projects_above_budget():
    budget = int(input("Enter budget for projects: "))
    query = f"""
    SELECT p.title, p.estimated_cost, r.name AS region_name
    FROM projects p
    JOIN regions r ON p.regions_id = r.regions_id
    WHERE p.estimated_cost > {budget};
    """
    result = execute_query(query, fetch='all')
    headers = ["Project Title", "Estimated Cost", "Region Name"]
    print(tabulate(result, headers=headers, tablefmt="fancy_grid"))


def get_total_budget():
    query = """
    SELECT SUM(estimated_cost) AS total_budget
    FROM projects;
    """
    result = execute_query(query, fetch='all')
    headers = ["Total Budget"]
    print(tabulate(result, headers=headers, tablefmt="fancy_grid"))


def search_project_by_letter():
    missing_letter = input("Enter letter to search for: ").strip().lower()
    query = f"""
    SELECT p.title, p.description, r.name AS region_name
    FROM projects p
    JOIN regions r ON p.regions_id = r.regions_id
    WHERE p.title LIKE '%{missing_letter}%';
    """
    result = execute_query(query, fetch='all')
    if result:
        headers = ["Project Title", "Description", "Region Name"]
        print(tabulate(result, headers=headers, tablefmt="fancy_grid"))
    else:
        print("No results found, sorry")


def show_all_categories():
    query = """ SELECT * FROM categories """
    result = execute_query(query, fetch='all')
    headers = ["ID", "Category Name"]
    print(tabulate(result, headers=headers, tablefmt="fancy_grid"))


