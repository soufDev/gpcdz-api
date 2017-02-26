#not finished yet

to launch the container you have to copy paste this instructions

    docker-compose build && docker-compose up -d

then if you want to create the database for the API you have to connect to the postgres container

    docker exec -ti mongodbdocker_postgres_1 bash

then copy paste this

    psql postgres postgres

then

    /q

after

    exit

after that you have to connect to django container

    docker exec -ti mongodbdocker_django_1 bash

then copy paste this:

    python manage.py makemigrations

    python manage.py migrate

after that you conect to

    http://localhost/geolocations

=> to see all the entite have been created

to see the uses whitch are stored on you mongodb container

    http://locahost/users => to see all the users that you have in mongodb container

or if you are running in a docker-machine like me replace localhost by your ip virtual machine

to post put & delete you have to go

    http://localhost/geolocation/id

    http://locahost/users/id or username


for the users post and put and delete doest not work I don't know I think its probleme with permissions








