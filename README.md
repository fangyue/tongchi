# tongchi

In order to run this website:<br />

Step 1:<br />
Install Django<br />

Step 2:<br />
Install MySQL: <br />
https://www.leeboonstra.com/developer/setup-a-django-project-with-a-mysql-database/<br />
Please set your username/password according to tongchi/settings.py<br />

Step 3:<br />
Initialize the database: <br />
In the tongchi project directory, <br />
$ python manage.py makemigrations <br />
$ python manage.py migrate <br />

Step 4:<br />
Run the server: <br />
python manage.py runserver <br />

Step 5:<br />
Open a browser to http://127.0.0.1:8000/ <br />


Dev log <br />
2017-11-2 by Weijie: pushed the first version of the backend <br />
    (1) basic login/logout/register features <br />
    (2) database API <br />
    (3) simple match workers (only for 2 people matching) <br />
