Required setup


System vars:

export APP_SETTINGS="config.DevelopmentConfig"
export DATABASE_URL="postgresql://localhost/wordcount_dev"



Need to Run stuff? We got that!

python app.py


Need Migrations? We got those!

    python manager.py db init
     - Create a fresh db
     - Actually alters db, so be ready
    python manager.py db migrate
     - Create a migration script from current state to state of current Models
     - Adds the new upgrade and downgrade migration to the migrations directory
    python manager.py db upgrade
     - Runs the migrations
     - Will alter the db, know what you're doing




Synopsis so far:
so python huh, you can only really talk about things below yourself in the heirarchy.
As a script you have no clue who called or where they are, just talk to things below you.
Counter intuitively, if there is something that you need globally, then it needs to be down the tree or in
the same directory as everything that needs it.

 - So 'db' is created with the models.
 - Then the api's create the Blueprint and manage getting the db (next level up)
  - The init in the api directory exposes db, the api, and the models to above packages.
 - Finally app gets the db and api from the v1 init


Todo:
?) public/private key stuff
?) basic auth stuff
?) Testing framework?!
?) Move the json stuff into the query helper
4) Figure out how to handle nested marshmallow schemas for load
 4.1) get rid of the double schema thing, maybe a post dump


Diddo:
1) Notetypes endpoints all working
2) Tenant endpoints all working
2) Note endpoints all working