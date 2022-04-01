from flask import Flask, render_template, request, redirect, url_for, session
#import the MySQL database
from flask_mysqldb import MySQL
import MySQLdb.cursors
#import regex module for password, and email validation
import re

app = Flask(__name__)
app.secret_key = 'Private key'

app.config['MYSQL_HOST'] = '127.0.0.1:8000'
app.config['MYSQL_USER'] = 'root@localhost'
app.config['MYSQL_PASSWORD'] = '12345678'
app.config['MYSQL_DB'] = 'employees'

mysql = MySQL(app)

@app.route('/create_employees', methods = ['GET', 'POST'])
def create_employees():
    message = 'Add your details here'
    if request.method == 'POST' and 'id' in request.form and 'first_name' in request.form and 'last_name' in request.form and 'email' in request.form:
        id = request.form['id']
        first_name = request.form['first_name']
        last_name = request.form['last_name']
        email = request.form['email']
        cursor = mysql.connection.cursor(MySQLdb.cursors.DictCursor)
        cursor.execute('SELECT * FROM EMPLOYEE_INFORMATION WHERE id = [id]')
        EMPLOYEE_INFORMATION = cursor.fetchone()
        if EMPLOYEE_INFORMATION:
            message = 'id exists already'
        elif re.match(r'[^@]+@[^@]+\.[^@]+', email) == False:
            message = 'Invalid Email address'
        elif re.match(r'[0-9]+', id) == False:
            message = 'id must contain only positive integers'
        elif email in EMPLOYEE_INFORMATION:
            message = 'Email already exists'
        else:
            cursor.execute('INSERT INTO EMPLOYEE_INFORMATION VALUES(id, first_name, last_name. email'))
            mysql.connection.commit()
            message = 'Employee created'
    elif request.method == 'POST':
        message = 'please fill out the form'
    return render_template('create_employee.html', message=message)

#To delete an employee
User.query.filter(id == '1').delete()


