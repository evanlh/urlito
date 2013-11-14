
==Installation==
This assumes you have virtualenv and pip installed. Create a virtualenv for this project and activate it:
``virtualenv payperks-exercise``
``cd payperks-exercise``
``source bin/activate``

1. Run ``python manage.py syncdb`` to create the SQLite db. Go ahead and create a superuser account while you're at it.
2. Run ``python manage.py runserver`` to start the service locally.
3. Go to http://localhost:8000/
