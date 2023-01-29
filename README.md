# FinalPythonAssignment
The final assignment for my Python course in the Data Science education. 

I'm going to use the following libraries to create my API:
- Django framework
- POSTMAN REST client for testing.
With inspiration from: https://www.simplifiedpython.net/django-rest-api-tutorial/


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

#-------------------------------------#

#-------------------------------------#
# Inlämingsuppgift python programering

## Mål och motivering

Målet är att vi ska skapa ett REST-API, kopplat till en databas, som vi seedar med data från en fil.

Motivering:
Enligt kursplanen ska vi lära oss koppla till en databas, lära oss att läsa från en fil samt lära oss hur vi använder paket. Vi ska också lära oss att interagera med API:er så detta är en bra möjlighet till att förstå hur de funkar.

## Instruktioner

Ni får använda valfritt bibliotek för att implementera API:et men jag kommer att ha visat med ett bibliotek som heter fastapi. I övrigt finns, django och flask exempelvis.

Jag kommer att ge er en modell som ni kan använda för databasen, ni får dock använda en egen om ni föredrar.

Ni kommer att få en fil med data relaterad till den modell jag ger er. Använder ni en egen så måste ni dock fixa denna fil själva för att kunna seeda databasen.

Vi kommer att ha byggt ett API under en av lektionerna och jag kommer att ha visat hur vi kan seeda databasen. För VG kan era lösningar inte vara för lika det från lektionen, och ingen kod får kopieras även om inspiration såklart får tas.

Skillnaden på G-kraven och VG-kraven är primärt det "självständiga" och med det så menar jag att ni ska ha gjort en egen lösning.

## Krav

API:

- Minst 2 "routes/endpoints" för att hämta olika typer av data
- Minst 2 "routes/endpoints" för att skapa data
- Minst 1 "route/endpoints" för att uppdatera data
- Minst 1 "route/endpoints" för att ta bort data
- Koppling till en databas

Övrigt:

- Logik för att seeda databasen från en fil (csv eller json), separat script eller annan lösning.
- Ett program som kan prata med API:et. Detta kan vara en enkel meny bara, likt vi gjort i några övningar.

! Icke fungerande kod betyder inte nödvändigtvis att ni inte får godkänt. Jag kommer att titta på er lösning och om jag ser att ni har tänkt på problemet och försökt lösa det på ett rimligt sätt, utan extrema fel, så kommer jag att godkänna er lösning. Jag vet att buggletande är tidskrävande. Rekomenderar att ni använder demot för att förklara hur ni tänkt och hur ni löst problemen.

## Demo

- Ni ska göra en demo av er lösning, 10-15 min
- Ni ska visa mig koden
- Ni ska förklara hur ni tänkt

STHLM: Onsdagen den 22/02/23
GBG: Torsdagen den 23/02/23

Demot kommer att ge er möjlighet till är att förklara hur ni tänkt och hur ni löst problemen. Detta kommer att ge er möjlighet att få visa att ni funderat över problemet på ett bra sätt även om koden kanske inte är helt korrekt. Så boka in en tid med mig så att vi kan göra en demo under den demo dag som finns för din klass.

## Inlämning

Deadline: 21/02/2023 - Tiden är oviktig men lämna in innan dagen tar slut
Omexamination 1, 2: Löpande inlämningar fram till 17/03/23
Få uppgiften klar till deadlinen då demo-tillfälle inte kan erbjudas efter.

Uppgiften måste lämnas in på omniway, men jag skulle föredra om ni skickar in en länk till ett github repo med koden på omniway istället för att lämna in exempelvis en zip fil.

Men då git inte är ett kurskrav så kommer jag att acceptera en zip fil om ni inte vill använda git.

## Övrigt

Jag kommer att vid frågor uppdatera den version som ligger på github men detta dokument komemr även att vara publicerat på omniway och teams. Ska försöka hålla alla uppdaterade men den på github är den som kommer att vara nyast.

Jag kan vid behov komma att lägga in lite tips eller svar på vanliga frågor här i uppgiften, men kommer isf att säga till.

Lycka till
