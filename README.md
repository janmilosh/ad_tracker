#Ad Tracker

An application for keeping track of newspaper advertisements.

## To Install Locally
Clone ad_tracker and navigate to project root.

Create virtual environment and install requirements:
```sh
mkvirtualenv ad_tracker
pip install -r requirements.txt
```

Note: if an error is thrown when installing the requirements, export CFLAGS and try again:
```sh
export CFLAGS=-Qunused-arguments && export CPPFLAGS=-Qunused-arguments
pip install -r requirements.txt
```

Create database:
```sh
createdb ad_tracker
```

Sync database and Django models:
```sh
python manage.py syncdb
```

## To run Locally (from within project root directory)
```sh
workon ad_tracker
python manage.py runserver
```