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





Todo:
1 - Move db instantiation elsewhere
2 - Separate models into independent files
3 - Decouple the db stuff a little (why do I need the same db in app and models?)