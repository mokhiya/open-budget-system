from tabulate import tabulate
from database_config.db_settings import execute_query


def add_categories():
    num_categories = int(input("How many categories do you want to insert? "))
    for i in range(num_categories):
        category_name = input(f"Enter name for category {i + 1}: ")
        query = """
        INSERT INTO categories (name)
        VALUES (%s)
        """
        execute_query(query, [category_name])
    print("Categories successfully added to database!")


def show_categories():
    query = """
    SELECT * FROM categories
    """
    categories = execute_query(query, fetch='all')
    headers = ["Category ID", "Name"]
    print(tabulate(categories, headers=headers))
    return categories


def update_category_name():
    show_categories()
    category_id = int(input("Enter the ID of the category you want to update: "))
    new_name = input("Enter the new name for the category: ")
    query = """
    UPDATE categories
    SET name = %s
    WHERE categories_id = %s
    """
    execute_query(query, [new_name, category_id])
    print("Category name successfully updated!")


def delete_category():
    show_categories()
    category_id = int(input("Enter the ID of the category you want to delete: "))
    query = """
    DELETE FROM categories
    WHERE categories_id = %s
    """
    execute_query(query, [category_id])
    print("Category successfully deleted!")

