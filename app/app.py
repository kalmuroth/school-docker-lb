from typing import List, Dict
from flask import Flask, render_template, redirect, url_for
import mysql.connector
import json

app = Flask(__name__)

#class Item:
#  def __init__(self, vals):
#    #self.__dict__ = vals
 #    for key, value in vals.items():
  #    setattr(self, key, value)

def tasks() -> List[Dict]:
    config = {
        'user': 'root',
        'password': 'root',
        'host': 'db',
        'port': '3306',
        'database': 'todo'
    }
    connection = mysql.connector.connect(**config)
    cursor = connection.cursor()
    cursor.execute('SELECT * FROM tasks')
    results = [{title: completed} for (title, completed) in cursor]
    print(results) # Afficher les résultats de la requête SQL
    cursor.close()
    connection.close()

    return results

@app.route('/')
def index():
    #return json.dumps({'tasks': tasks()}) 
    return render_template('index.html', text=tasks())
    #data = tasks()
    #return render_template('index.html', text=[Item(i) for i in data])

@app.route('/delete/<title>', methods=['POST'])
def delete(title):
    config = {
        'user': 'root',
        'password': 'root',
        'host': 'db',
        'port': '3306',
        'database': 'todo'
    }
    connection = mysql.connector.connect(**config)
    cursor = connection.cursor()
    query = "DELETE FROM tasks WHERE title = %s"
    cursor.execute(query, (title,))
    connection.commit()
    cursor.close()
    connection.close()
    
    return redirect(url_for('index'))


if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True)
