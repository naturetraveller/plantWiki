import pandas as pd
import sqlite3

def import_excel_to_sqlite(excel_file, sqlite_db):
    # Read the Excel file into a pandas DataFrame
    df = pd.read_excel(excel_file, sheet_name="Sheet1")

    # Connect to the SQLite database
    conn = sqlite3.connect(sqlite_db)
    cursor = conn.cursor()

    # Create the "wikiPlants" table in the database
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS wikiPlants (
            "LateinischerName" TEXT,
            "DeutscherName" TEXT,
            "Gattung" TEXT,
            "Familie" TEXT,
            "Ordnung" TEXT,
            "Klasse" TEXT,
            "Stamm" TEXT,
            "Reich" TEXT,
            "Bild" BLOB,
            "Bild 2" BLOB,
            "Bild 3" BLOB
        )
    ''')

    # Insert the data into the "wikiPlants" table
    for row in df.itertuples(index=False):
        cursor.execute('''
            INSERT INTO wikiPlants VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
        ''', row)

    # Commit the changes and close the database connection
    conn.commit()
    conn.close()

# Provide the path to your Excel file and SQLite database
excel_file_path = 'C:/Users/ahael/Meine Ablage/bio.sysbio/wikiPlants.xlsx'
sqlite_db_path = 'C:/Users/ahael/Meine Ablage/websites/gitHub/plantWiki/wikiPlants.db'

# Call the function to import the Excel data into SQLite
import_excel_to_sqlite(excel_file_path, sqlite_db_path)
