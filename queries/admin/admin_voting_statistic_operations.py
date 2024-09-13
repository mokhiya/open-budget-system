from tabulate import tabulate
from database_config.db_settings import execute_query


def show_all_voted_projects():
    """
    This function shows all voted projects
    """
    print("Voted projects:\n")
    query = """
        SELECT p.projects_id, p.title, COUNT(v.voting_id) AS vote_count
        FROM projects p
        JOIN voting v ON p.projects_id = v.projects_id
        GROUP BY p.projects_id, p.title
        ORDER BY vote_count DESC;
    """
    result = execute_query(query, fetch='all')
    headers = ["Project ID", "Title", "Vote Count"]
    if result:
        print(tabulate(result, headers=headers, tablefmt="fancy_grid"))
    else:
        print("No projects have been voted on yet.")


def show_all_non_voted_projects():
    """
    This function shows all non-voted projects
    """
    print("Non-voted projects:\n")
    query = """
        SELECT p.projects_id, p.title
        FROM projects p
        LEFT JOIN voting v ON p.projects_id = v.projects_id
        WHERE v.voting_id IS NULL
        ORDER BY p.title;
    """
    result = execute_query(query, fetch='all')
    headers = ["Project ID", "Title"]
    if result:
        print(tabulate(result, headers=headers, tablefmt="fancy_grid"))
    else:
        print("All projects have received votes.")


def get_winners():
    """
    This function shows all winners
    """
    query = """
    SELECT vc.categories_id, vc.projects_id, vc.title, vc.vote_count
    FROM 
        (SELECT p.categories_id, p.projects_id, p.title,
            COUNT(v.voting_id) AS vote_count
        FROM projects p
        JOIN 
            voting v ON p.projects_id = v.projects_id
        GROUP BY 
            p.categories_id, p.projects_id, p.title) AS vc
    JOIN 
        (SELECT categories_id, MAX(vote_count) AS max_votes
        FROM 
            (SELECT p.categories_id, p.projects_id, COUNT(v.voting_id) AS vote_count
            FROM projects p
            JOIN 
                voting v ON p.projects_id = v.projects_id
            GROUP BY p.categories_id, p.projects_id) AS vote_counts
        GROUP BY categories_id) AS max_votes_per_category
    ON 
        vc.categories_id = max_votes_per_category.categories_id
    AND 
        vc.vote_count = max_votes_per_category.max_votes;
    """
    result = execute_query(query, fetch='all')
    print("Winners:\n")
    headers = ["Category ID", "Project ID", "Title", "Vote Count"]
    print(tabulate(result, headers=headers, tablefmt="fancy_grid"))
    return result


