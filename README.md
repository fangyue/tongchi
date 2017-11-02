# tongchi
# tongchi

In order to run this website:

Step 1:
Install Django

Step 2:
Install MySQL: 
https://www.leeboonstra.com/developer/setup-a-django-project-with-a-mysql-database/
Please set your username/password according to tongchi/settings.py

Step 3:
Initialize the database:
In the tongchi project directory,
$ python manage.py makemigrations
$ python manage.py migrate

Step 4:
Run the server:
python manage.py runserver

Step 5:
Open a browser to http://127.0.0.1:8000/
