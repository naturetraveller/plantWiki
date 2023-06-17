import sqlite3

def empty_table(sqlite_db, table_name):
    # Connect to the SQLite database
    conn = sqlite3.connect(sqlite_db)
    cursor = conn.cursor()

    # Delete all entries in the table
    delete_query = f'DELETE FROM {table_name}'
    cursor.execute(delete_query)

    # Commit the changes and close the database connection
    conn.commit()
    conn.close()

# Provide the path to your SQLite database
sqlite_db_path = 'C:/Users/ahael/Meine Ablage/websites/gitHub/plantWiki/wikiPlants.db'

# Specify the table name
table_name = 'wikiPlants'

# Call the function to empty the table in the SQLite database
empty_table(sqlite_db_path, table_name)
