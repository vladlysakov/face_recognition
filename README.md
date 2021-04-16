# Face Recognition using Django


# HOW TO RUN APPLICATION:

**REQUIRED MODULES**

`
    Once the project has been pulled the first step is install the required modules by following command:
    "[pip or pip3] install -r requirements.txt"
    But be sure you are in correct project's folder.
`


**DATABASE**
`
    This app runs on Django and uses PostgreSQL database. 
    It is not a problem to use another database. 
    If you want to use it, you should change the database settings in settings.py file in project folder.
    You should create a database with name "face_recognition" or input you own name to the settings file.
    Once the database has been created these commands must be executed in terminal:
`

    "python<your_version> manage.py makemigrations face"
    "python<your_version> manage.py migrate"
`
    But be sure you are in correct project's folder.
`

**SUPERUSER**

`
    If the database is installed and configured successfully, the next step is to create a superuser by running the 
    following command:
    "pytho<your_version> manage.py createsuperuser"
`

**RUN PROJECT**
`
    The project runs by command:
    "pytho<your_version> manage.py runserver <host>:<port>"
    But do not forget this data about host and port must be in project's settings file 
`
