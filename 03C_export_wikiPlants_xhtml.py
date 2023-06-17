import sqlite3

def export_data_to_xhtml():
    conn = sqlite3.connect('wikiPlants.db')
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM wikiPlants')
    data = cursor.fetchall()
    conn.close()

    with open('wikiPlants_data.xhtml', 'w') as file:
        file.write('<?xml version="1.0" encoding="UTF-8"?>\n')
        file.write('<!DOCTYPE html PUBLIC "-//W3C//DTD XHTML 1.0 Strict//EN" "http://www.w3.org/TR/xhtml1/DTD/xhtml1-strict.dtd">\n')
        file.write('<html xmlns="http://www.w3.org/1999/xhtml">\n')
        file.write('<head>\n')
        file.write('<title>Wiki Plants Data</title>\n')
        file.write('</head>\n')
        file.write('<body>\n')
        file.write('<h1>Wiki Plants Data</h1>\n')
        file.write('<table>\n')
        file.write('<tr>\n')
        file.write('<th>Latin Name</th>\n')
        file.write('<th>Deutscher Name</th>\n')
        file.write('<th>Gattung</th>\n')
        file.write('<th>Familie</th>\n')
        file.write('<th>Ordnung</th>\n')
        file.write('<th>Klasse</th>\n')
        file.write('<th>Stamm</th>\n')
        file.write('<th>Reich</th>\n')
        file.write('</tr>\n')

        for row in data:
            file.write('<tr>\n')
            file.write(f'<td>{row[0]}</td>\n')
            file.write(f'<td>{row[1]}</td>\n')
            file.write(f'<td>{row[2]}</td>\n')
            file.write(f'<td>{row[3]}</td>\n')
            file.write(f'<td>{row[4]}</td>\n')
            file.write(f'<td>{row[5]}</td>\n')
            file.write(f'<td>{row[6]}</td>\n')
            file.write(f'<td>{row[7]}</td>\n')
            file.write('</tr>\n')

        file.write('</table>\n')
        file.write('</body>\n')
        file.write('</html>\n')

    print("Die Daten wurden erfolgreich in die Datei 'wikiPlants_data.xhtml' exportiert.")

export_data_to_xhtml()
