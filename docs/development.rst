Development
===========

Requirements
------------

* `python`_ 2.7, `virtualenv`_, & `pip`_ for app server
* `elasticsearch`_

.. _python: https://www.python.org/
.. _virtualenv: http://docs.python-guide.org/en/latest/dev/virtualenvs/
.. _pip: https://pip.readthedocs.org/en/latest/
.. _elasticsearch: https://www.elastic.co/products/elasticsearch


Install Locally
---------------

#. `Clone`_ and change to the directory::

    git clone git@github.com:codefortulsa/city-struggle-bus.git
    cd city-struggle-bus

#. Create and activate a `virtual environment`_ (Can also use `virtualenvwrapper`_)::

    virtualenv env
    source env/bin/activate

#. `Install requirements`_::

    pip install -r requirements.txt

#. Source the ``.env`` file to set environment config vars (Can also use `autoenv`_)::

    source .env

#. `Migrate`_ DB tables ::

    python manage.py migrate

#. `Create a superuser`_::

    python manage.py createsuperuser

.. _Clone: http://git-scm.com/book/en/Git-Basics-Getting-a-Git-Repository#Cloning-an-Existing-Repository
.. _Install requirements: http://pip.readthedocs.org/en/latest/user_guide.html#requirements-files
.. _Migrate: https://docs.djangoproject.com/en/1.9/topics/migrations/
.. _Create a superuser: https://docs.djangoproject.com/en/1.9/ref/django-admin/#django-admin-createsuperuser


Run it
------

#. Source the ``.env`` file to set environment config vars (Can also use `autoenv`_)::

    source .env

#. Activate the `virtual environment`_ (Can also use `virtualenvwrapper`_)::

    source env/bin/activate

#. Run it::

    python manage.py runserver


Run the Tests
-------------
#. Install test requirements::

    pip install -r requirements-test.txt

#. Running the test suite::

    python manage.py test


Working on Docs
---------------
Install doc requirements::

    pip install -r requirements-docs.txt

Building the docs is easy::

    cd docs
    sphinx-build . html

Read the beautiful docs::

    open html/index.html


What to work on
---------------

We have `Issues`_.

.. _Issues: https://github.com/codefortulsa/city-struggle-bus/issues

.. _virtual environment: http://docs.python-guide.org/en/latest/dev/virtualenvs/
.. _virtualenvwrapper: https://pypi.python.org/pypi/virtualenvwrapper
.. _autoenv: https://github.com/kennethreitz/autoenv
