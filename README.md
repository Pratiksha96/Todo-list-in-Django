#TO-DO LIST

##Python version 2.7 is required.
##Django version 1.9 or greater required to run this project.
##MySql version 5.7 is used.

To run this project follow given steps:

1. Clone the project into your working directory.
2. Create a virtual environment and install dependencies.
	
	mkvirtualenv new_project
3. Duplicate task/task/settings.py and save as local_settings.py.
4. Enter your database settings in local_settings.py.
5. Initialize your database.
	
	python ./manage.py syncdb
	python ./manage.py migrate

6. Since, our app has a custom user model, you'll need to create a new superuser for the admin.
	
	python ./manage.py createsuperuser

7. Run the development server to verify everything is working.

	python ./manage.py runserver