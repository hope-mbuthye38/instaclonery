## TITLE
INSTACLONERY

# #Author
Hope Mbuthye

## Description

Instaclonery is simply a clone of the website for the popular photo app Instagram

# User stories
As a user I should be able to:

Sign in to the application to start using.

Upload my pictures to the application.

See my profile with all my pictures.

Follow other users and see their pictures on my timeline.

Like a picture and leave a comment on it.

# BUILD
Clone the repositories git clone:[ (instanry)[https://github.com/hope-mbuthye38/instaclonery.git]]

Open root directory and install requirements python -m pip install -r requirements.txt

Export configurations export SQLALCHEMY_DATABASE_URI=postgresql+psycopg2://{User Name}:{password}
@localhost/{database name}

Run the application python3.8 manage.py runserver

Run tests on the application python3.8 manage.py tests

 # #Setup instructions

 ## Requirements

1. Create a django and create django projects

2. Create a virtual environment

 1. Install a virtual environment

2. python3.8 -m venv Virtual
To activate the virtual environment we just created, run

source virtual/bin/activate

3. pip install django==2.2

1. Create django project

django-admin startproject instapp .

2. create django app 

django-admin startapp instanry

3. Create a database
You'll need to create a new postgress database, Type the following command to access postgress

 $ psql
Then run the following query to create a new database named insta

# create database instanry
4.Install dependencies
To install the requirements from requirements.txt file,

pip install -r requirements.txt
5.Create Database migrations
Making migrations on postgres using django

python manage.py makemigrations gallery
then run the command below;

python manage.py migrate
6.Run the app
To run the application on your development machine,

python manage.py runserver
 # Technologies Used
1. Django
2. Python
3. Html
4. Css 
5. Bootstrap4
Django-Admin
# Bugs
Displaying posts and some functionality of likes and follow

# License


MIT license © 2021 Hope Mbuthye

# Collaboration Information
1. Clone the repository
2. Make changes and write tests
3. Push changes to github

 # #Contacts
Tel no 0785493051
email hope.mbuthye39@gmail.com