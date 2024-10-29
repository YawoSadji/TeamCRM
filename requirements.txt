Create a virtual environment
    python -m venv <virtual environment name>
Activate virtual environment
    for mac:   source <virtual environment name>/bin/activate
    for windows: source <virtual environment name>/Scripts/activate
Install dependencies
    pip install django
    (using mysql as database here)
    pip install mysql
    pip install mysql-connector-python
    Install mysql installer : https://dev.mysql.com/downloads/installer/
Create database
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
run python <filename> (python crmdb.py for example)

Run python manage.py migrate to apply migrations
Create a superuser to manage users in django admin portal
    for windows: winpty python manage.py createsuperuser
    for mac: python manage.py createsuperuser
Run the website: python manage.py runserver