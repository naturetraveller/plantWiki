import pandas as pd
import sqlite3

def update_table_from_excel(excel_file, sqlite_db):
    # Read the Excel sheet named 'Sheet1' into a pandas DataFrame
    df = pd.read_excel(excel_file, sheet_name='Sheet1')

    # Connect to the SQLite database
    conn = sqlite3.connect(sqlite_db)
    cursor = conn.cursor()

    # Get the existing Latin names from the database
    cursor.execute('SELECT "LateinischerName" FROM wikiPlants')
    existing_names = set(row[0] for row in cursor.fetchall())

    # Filter the DataFrame to include only new entries
    new_entries = df[~df['LateinischerName'].isin(existing_names)]

    # Update the table with new entries
    for row in new_entries.itertuples(index=False):
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

# Call the function to update the table in the SQLite database from the Excel data
update_table_from_excel(excel_file_path, sqlite_db_path)
