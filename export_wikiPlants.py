from flask import Flask, render_template
import sqlite3
import os

app = Flask(__name__)

def get_data_from_database():
    conn = sqlite3.connect('wikiPlants.db')
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM wikiPlants')
    data = cursor.fetchall()
    conn.close()
    return data

def create_template():
    conn = sqlite3.connect('wikiPlants.db')
    cursor = conn.cursor()
    cursor.execute("PRAGMA table_info(wikiPlants)")
    columns = cursor.fetchall()
    column_names = [column[1] for column in columns]
    
    template = '''
    <!DOCTYPE html>
    <html>
    <head>
        <title>Plant Wiki</title>
    </head>
    <body>
        <h1>Plant Wiki</h1>
        <table>
            <tr>
            {% for column in columns %}
                <th>{{ column }}</th>
            {% endfor %}
            </tr>
            {% for row in data %}
            <tr>
                {% for column in row %}
                <td>{{ column }}</td>
                {% endfor %}
            </tr>
            {% endfor %}
        </table>
    </body>
    </html>
    '''
    
    with open('wikiPlants.html', 'w') as file:
        file.write(render_template_string(template, columns=column_names, data=get_data_from_database()))

@app.route('/')
def index():
    if not os.path.isfile('wikiPlants.html'):
        create_template()
    return render_template('wikiPlants.html')

if __name__ == '__main__':
    app.run()
