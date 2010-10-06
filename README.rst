Djangobench WebUI
=================

djangobench-webui is a django app to visualize the results of the `djangobench`_ benchmark suite.

.. _`djangobench`: http://github.com/jacobian/djangobench

Installation
============

This is a quick and dirty installation to get up and running.  I've included all
the javascript libraries and enabled django to serve static files.  Just
change to the directory where you want your virtualenv and enter the following
commands::

    virtualenv --no-site-packages djangobench
    cd djangobench
    . bin/activate
    pip install -e git+git://github.com/sebleier/djangobench-webui.git#egg=djangobench-webui
    pip install -e git+git://github.com/jacobian/djangobench.git#egg=djangobench
    mkdir results
    git clone git://github.com/django/django.git
    cd django
    djangobench --vcs=git --control=1.2 --experiment=master --record ../results
    cd ../src/djangobench-webui/djangobench_webui
    python manage.py runserver
