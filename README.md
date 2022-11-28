# University Events Inventory

## Setup

The first thing to do is to clone the repository:

```sh
$ git clone https://github.com/somyaranjan26/UniversityEvents.git
$ cd code
```

Create a virtual environment to install dependencies in and activate it:

```sh
$ virtualenv2 --no-site-packages env
$ source env/bin/activate
```

Then install the dependencies:

```sh
(env)$ pip install -r requirements.txt
```
Note the `(env)` in front of the prompt. This indicates that this terminal
session operates in a virtual environment set up by `virtualenv2`.

Once `pip` has finished downloading the dependencies:
```sh
(env)$ cd project
(env)$ python manage.py runserver
```
And navigate to `http://127.0.0.1:8000/`.

Replace your own S3 Bucket creadentials in the end of `settings.py` file

```sh
AWS_ACCESS_KEY_ID = 'AKIA************'
AWS_SECRET_ACCESS_KEY = 'Oz/RGvQi1ETS************'
AWS_STORAGE_BUCKET_NAME = 'your-bucket-name'
```