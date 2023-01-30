Step 1: create a Django project

    1.1 install django
            python -m pip install --user django (in a powershell with admin rights)
            pip install django (in terminal powershell in VS code)

    1.2 make django project ( THIS is the api, server, the backend)
            python -m django startproject CraftBeerAPI (in terminal powershell in VS code) 

    1.3 test server
            cd .\CraftBeerAPI\
            python manage.py runserver

            -> runs on : http://127.0.0.1:8000/

Step 2: open that project and install Django REST Framework

    2.1 install the REST framework for django
        pip install djangorestframework

    2.2 make an app inside there that starts the application
        python manage.py startapp CraftBeerInfoApp

Step 3: configure settings in the project
    
    3.1 in: settings.py
        add two new lines: see below.
        INSTALLED_APPS = [
            'rest_framework',
            'CraftBeerInfoApp'
        ]

Step 4: create my model for the database
    
    4.1 add into CraftBeerInfo\CraftBeerInfoApp\models.py ( some info about the tables / columns) 
        ex: class beer(models.Model):
                name = models.CharField(max_length=10)


Step 5: register models to the admin file

    5.1 add to admin.py ( some info about the model to add to the db)
        # Register your models here.
        from .models import beer
        # Register your models here.
        admin.site.register(beer)

Step 6: migrate ( in FinalPythonAssignment\CraftBeerAPI )

    6.1 update your table structure.
        python manage.py makemigrations
    6.2 create your table with current structure and it will fills all the details that you have written in your model
        python manage.py migrate

Step 7: create superuser

    7.1 python manage.py createsuperuser
    admin
    1234

Step 8: Run app and see on url the output

    8.1 run the server
        python manage.py runserver
    8.2 login as an admin
        http://127.0.0.1:8000/admin/

Step 9: Change the look of the page

    9.1 add a view to view.py file

    9.3 add url to the view in the urls.py file

Step 10: add data from csv file to beer model
    10.1 update model with correct column names
    10.2 migrate
    10.3 scripts folder(with init)
    10.4 test to load csv into data frame.
    10.5 pip install django-seed   pip install fsspec

Step 11: make html template
    11.1 make new folder and a html file which loops data
    12.2 adjust view to link to the template.
    (12.3 in admin view add one test object to test. if seed has not worked properly)

#-------------------------------------#