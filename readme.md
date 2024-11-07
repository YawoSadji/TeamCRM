# TeamCRM
TeamCRM is a contact management website for small teams.

## Installation
1.Create a virtual environment
    python -m venv <virtual environment name>
Activate virtual environment
    for mac:   source <virtual environment name>/bin/activate
    for windows: source <virtual environment name>/Scripts/activate
2.Install dependencies(use pip package manager)
    pip install django
    (using mysql as database here)
    pip install mysql
    pip install mysql-connector-python
    Install mysql installer : https://dev.mysql.com/downloads/installer/
3.Create database
    create a file (crmdb.py for example)
    Inside the file, import mysql.connector
    add your configuration:
    connection = mysql.connector.connect(
        user='your_user_name',
        password='your_password',
        host='localhost'
    )
    cursor = connection.cursor()
    cursor.execute("CREATE DATABASE your_database_name")
4.run python <filename> (python crmdb.py for example)

5.Run python manage.py migrate to apply migrations
6.Create a superuser to manage users in django admin portal
    for windows: winpty python manage.py createsuperuser
    for mac: python manage.py createsuperuser
7.Run the website: python manage.py runserver

##License
https://choosealicense.com/licenses/mit/