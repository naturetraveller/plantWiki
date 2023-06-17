import pandas as pd
import sqlite3

def import_excel_to_sqlite(excel_file, sqlite_db):
    # Read the Excel file into a pandas DataFrame
    df = pd.read_excel(excel_file, sheet_name="Sheet1")

    # Connect to the SQLite database
    conn = sqlite3.connect(sqlite_db)
    cursor = conn.cursor()

    # Check if a row already exists in the table based on 'LateinischerName'
    existing_rows = set(cursor.execute('SELECT "LateinischerName" FROM wikiPlants').fetchall())

    # Insert new data into the "wikiPlants" table
    for row in df.itertuples(index=False):
        if (row[0],) not in existing_rows:
            cursor.execute('''
                INSERT INTO wikiPlants ("LateinischerName", "DeutscherName", "Gattung", "Familie", "Ordnung", "Klasse", "Stamm", "Reich", "Bild", "Bild 2", "Bild 3")
                VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
            ''', row)

    # Commit the changes and close the database connection
    conn.commit()
    conn.close()

# Provide the path to your Excel file and SQLite database
excel_file_path = 'C:/Users/ahael/Meine Ablage/bio.sysbio/wikiPlants.xlsx'
sqlite_db_path = 'C:/Users/ahael/Meine Ablage/websites/gitHub/plantWiki/wikiPlants.db'

# Call the function to import the Excel data into SQLite, skipping existing rows
import_excel_to_sqlite(excel_file_path, sqlite_db_path)
