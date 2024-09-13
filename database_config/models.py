from database_config.db_settings import execute_query


def create_table():
    query = """
    CREATE TABLE IF NOT EXISTS regions (
        regions_id BIGSERIAL PRIMARY KEY NOT NULL,
        name VARCHAR NOT NULL
    );

    CREATE TABLE IF NOT EXISTS categories (
        categories_id BIGSERIAL PRIMARY KEY NOT NULL,
        name VARCHAR NOT NULL
    );
    

    CREATE TABLE IF NOT EXISTS districts (
        districts_id BIGSERIAL PRIMARY KEY,
        regions_id BIGINT NOT NULL,
        name VARCHAR NOT NULL,
        FOREIGN KEY (regions_id) REFERENCES regions(regions_id)
    );


    CREATE TABLE IF NOT EXISTS users (
        users_id BIGSERIAL PRIMARY KEY NOT NULL,
        full_name VARCHAR NOT NULL,
        phone_number VARCHAR NOT NULL UNIQUE,
        login VARCHAR NOT NULL,
        password VARCHAR NOT NULL,
        is_login BOOLEAN NOT NULL DEFAULT FALSE
    );
    
    
    CREATE TABLE IF NOT EXISTS statuses (
        statuses_id BIGSERIAL PRIMARY KEY NOT NULL,
        status_name VARCHAR NOT NULL
    );
    
    
    CREATE TABLE IF NOT EXISTS projects (
        projects_id UUID PRIMARY KEY NOT NULL DEFAULT uuid_generate_v4(),
        users_id BIGINT NOT NULL,
        categories_id BIGINT NOT NULL,
        title VARCHAR NOT NULL,
        description TEXT,
        regions_id BIGINT NOT NULL,
        districts_id BIGINT NOT NULL,
        community_name TEXT NOT NULL,
        estimated_cost FLOAT,
        submitted_at TIMESTAMP,
        statuses_id BIGINT NOT NULL,
    FOREIGN KEY (users_id) REFERENCES users(users_id),
    FOREIGN KEY (categories_id) REFERENCES categories(categories_id),
    FOREIGN KEY (regions_id) REFERENCES regions(regions_id),
    FOREIGN KEY (districts_id) REFERENCES districts(districts_id),
    FOREIGN KEY (statuses_id) REFERENCES statuses(statuses_id)
);
    
    
    CREATE TABLE IF NOT EXISTS seasons (
        seasons_id BIGSERIAL PRIMARY KEY NOT NULL,
        name VARCHAR NOT NULL,
        is_active BOOLEAN NOT NULL DEFAULT FALSE,
        start_date TIMESTAMP NOT NULL,
        end_date TIMESTAMP NOT NULL
    );

    CREATE TABLE IF NOT EXISTS voting (
    voting_id BIGSERIAL PRIMARY KEY NOT NULL,
    seasons_id BIGINT NOT NULL,
    users_id BIGINT NOT NULL,
    projects_id UUID NOT NULL,
    FOREIGN KEY (seasons_id) REFERENCES seasons(seasons_id),
    FOREIGN KEY (users_id) REFERENCES users(users_id),
    FOREIGN KEY (projects_id) REFERENCES projects(projects_id)
    );
    """
    execute_query(query)
    print("Database tables created successfully")


