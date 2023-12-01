from typing import List, Dict
from flask import Flask, render_template, redirect, url_for
import mysql.connector
import json

app = Flask(__name__)

def getData() -> List[Dict]:
    config = {
        'user': 'root',
        'password': 'root',
        'host': 'db',
        'port': '3306',
        'database': 'test'
    }
    connection = mysql.connector.connect(**config)
    cursor = connection.cursor()
    cursor.execute('SELECT * FROM data')
    results = [{name: value} for (name, value) in cursor]
    cursor.close()
    connection.close()

    return results

@app.route('/')
def index():
    return render_template('index.html', text=getData())

@app.route('/delete/<name>', methods=['POST'])
def delete(name):
    config = {
        'user': 'root',
        'password': 'root',
        'host': 'db',
        'port': '3306',
        'database': 'test'
    }
    connection = mysql.connector.connect(**config)
    cursor = connection.cursor()
    query = "DELETE FROM name WHERE name = %s"
    cursor.execute(query, (name,))
    connection.commit()
    cursor.close()
    connection.close()
    
    return redirect(url_for('index'))


if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True)
