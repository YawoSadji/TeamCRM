# TeamCRM
TeamCRM is a contact management website for small teams.

## Installation

1. **Create a virtual environment:**
   ```
   python -m venv <virtual environment name>
   ```
   **Activate virtual environment:**
   - For macOS/Linux:
     ```
     source <virtual environment name>/bin/activate
     ```
   - For Windows:
     ```
     source <virtual environment name>/Scripts/activate
     ```

2. **Install dependencies (using pip):**
   ```
   pip install -r requirements.txt
   ```

3. **Database Setup:**
   - **Default:** The project is configured to use **PostgreSQL** by default (see `main/settings.py`).
   - **Environment Variables:** Set your PostgreSQL connection string in the `DATABASE_URL` environment variable. Example:
     ```
     export DATABASE_URL=postgres://USER:PASSWORD@HOST:PORT/DBNAME
     ```
   - **Alternative (MySQL):** If you want to use MySQL, update the `DATABASE_URL` accordingly and ensure the required MySQL packages are installed.

4. **Apply migrations:**
   ```
   python manage.py migrate
   ```

5. **Create a superuser to manage users in the Django admin portal:**
   - For Windows:
     ```
     winpty python manage.py createsuperuser
     ```
   - For macOS/Linux:
     ```
     python manage.py createsuperuser
     ```

6. **Run the website:**
   ```
   python manage.py runserver
   ```

## License
[MIT](https://choosealicense.com/licenses/mit/)