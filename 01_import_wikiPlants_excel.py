import pandas as pd
import sqlite3

def import_excel_to_sqlite(excel_file, sqlite_db):
    # Read the Excel file into a pandas DataFrame
    df = pd.read_excel(excel_file)

    # Connect to the SQLite database
    conn = sqlite3.connect(sqlite_db)
    cursor = conn.cursor()

    # Create the "wikiPlants" table in the database
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS wikiPlants (
            "Latin Name" TEXT,
            "Deutscher Name" TEXT,
            "Gattung" TEXT,
            "Familie" TEXT,
            "Ordnung" TEXT,
            "Klasse" TEXT,
            "Stamm" TEXT,
            "Reich" TEXT
        )
    ''')

    # Insert the data into the "wikiPlants" table
    for row in df.itertuples(index=False):
        cursor.execute('''
            INSERT INTO wikiPlants VALUES (?, ?, ?, ?, ?, ?, ?, ?)
        ''', row)

    # Commit the changes and close the database connection
    conn.commit()
    conn.close()

# Provide the path to your Excel file and SQLite database
excel_file_path = 'path/to/your/excel_file.xlsx'
sqlite_db_path = 'path/to/your/database.db'

# Call the function to import the Excel data into SQLite
import_excel_to_sqlite(excel_file_path, sqlite_db_path)
