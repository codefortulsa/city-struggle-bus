Deployment
==========

city-struggle-bus is designed with `12-factor app philosophy`_ to run on
`heroku`_, so you can easily deploy your changes to your own heroku app with
`heroku toolbelt`_.


Deploy your own
---------------

#. `Create a heroku remote`_. We suggest naming it moz-dev-dash-`username`::

    heroku apps:create moz-dev-dash-username

#. Push code to the heroku remote::

    git push heroku master

#. `Migrate`_ DB tables on heroku::

    heroku run python manage.py migrate

#. Create a superuser on heroku::

    heroku run python manage.py createsuperuser

#. Open the new heroku app::

    heroku open


.. _12-factor app philosophy: http://12factor.net/
.. _heroku: https://www.heroku.com/
.. _heroku toolbelt: https://toolbelt.heroku.com/
.. _Create a heroku remote: https://devcenter.heroku.com/articles/git#creating-a-heroku-remote
