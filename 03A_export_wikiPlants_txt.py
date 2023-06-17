import sqlite3

def export_data_to_file():
    conn = sqlite3.connect('wikiPlants.db')
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM wikiPlants')
    data = cursor.fetchall()
    conn.close()

    with open('wikiPlants_data.txt', 'w') as file:
        for row in data:
            file.write(f'Latin Name: {row[0]}\n')
            file.write(f'Deutscher Name: {row[1]}\n')
            file.write(f'Gattung: {row[2]}\n')
            file.write(f'Familie: {row[3]}\n')
            file.write(f'Ordnung: {row[4]}\n')
            file.write(f'Klasse: {row[5]}\n')
            file.write(f'Stamm: {row[6]}\n')
            file.write(f'Reich: {row[7]}\n')
            file.write('\n')

    print("Die Daten wurden erfolgreich in die Datei 'wikiPlants_data.txt' exportiert.")

export_data_to_file()
