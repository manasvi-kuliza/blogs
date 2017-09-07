# Installation Guide #

### Dependencies ###

* Python 3.x
* PostGreSQL

### Getting Started ###

* Create a user for postgres : "createuser <username> --pwprompt"
* Create a db for the application : "createdb blogs"
* Set password for the database : <DB_PASSWORD>


### Virtual Environment Setup ###

* Setup virtualenv : "virtualenv -p python3 blogs_env"
* Move to virtualenv and activate its environment
* Take pull from the repo and move to the directory
* Change DB settings in blogs/settings.py file
* Run "pip install -r requirements.txt" to set up dependent libraries
* Run migration by : "python manage.py migrate"
* Run server by : "python manage.py runserver"