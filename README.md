## Contact Importer

### Prerequisites
+ Node >= v14.17.0
+ NPM >= 6.14.13
+ docker >= 20.10.14
+ docker-compose >= 1.29.2

### Clone both repositories
#### [Frontend](https://github.com/JoseJuanCM/fe-contact-importer)
#### [Backend](https://github.com/JoseJuanCM/contact-importer)

### Backend
+ Open a terminal in the root of the repository run the following commands
  ```
  docker-compose -f local.yml build 
  docker-compose -f local.yml run --rm django python manage.py migrate
  docker-compose -f local.yml run --rm django python manage.py loaddata crontabs
  docker-compose -f local.yml run --rm django python manage.py loaddata intervals
  docker-compose -f local.yml run --rm django python manage.py loaddata tasks
  docker-compose -f local.yml run --rm django python manage.py createsuperuser
  docker-compose -f local.yml up
  ```

### Frontend
+ In other terminal in the root of the repository run
  + `npm i`
  + `npm run dev`
+ In the assets folder you will find a CSV test file, copy it into your desktop
  + Go to you [localhost](http://localhost:3000/)
  + Anytime you can click in the logo to go to the [main menu](http://localhost:3000/)
  + You must see the Login form
    + You can log in with the superuser credentials you created previously
    + If you click in the Sign-Up button you can create a new user with email and password
      + _After submit the new user information you'll be redirected to the login form_
    + After login, you will be able to see the main menu
      + Click on [Load New File](http://localhost:3000/load)
      + Load the file you copied from the assets folder
      + Fill out the headers names with the next keywords
      ```
      Nombre
      Dir
      Cumple
      Tarjeta
      Cel
      correo
      ```
      + After load the file you will be redirected to the files page
        + You will see a table with all the files loaded and their status
        + ### Note: The task to process the files runs every 5 minutes
          + You must refresh the page to validate the new status
        + If you click in the Errors Detail you will be able to view all the records of the file that has errors and were not loaded
            
      + Go to the [contacts page](http://localhost:3000/contacts) to view the list of all the contacts processed
  
