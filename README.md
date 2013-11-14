Installation
============

This assumes you have virtualenv and pip installed. Create a virtualenv for this project and activate it:

    $ virtualenv payperks-exercise
    $ cd payperks-exercise
    $ source bin/activate

Create and initialize the SQLite db. Go ahead and create a superuser account while you're at it.

    $ python manage.py syncdb

Start the service locally.

    $ python manage.py runserver

Go to http://localhost:8000/ and shorten URLs to your heart's content!

Some Notes On Implementation
============================

URLs are encoded as base 62, their shortened URL in a one to one correspondence with the the primary key ID in the database. In this implementation, the earliest URLs will have the shortest base62 abbreviation, the reads will be fast but the writes are doubled. There are many ways of approaching the issue of key generation & cache collision management, this is the quick-and-dirty one. I implemented this site using Django to refamiliarize myself with it, although for a project of this size Flask would probably be the more appropriate framework.
