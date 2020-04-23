# Web app NLP

Full stack Developer challenge.

I created an intuitive and practical web application to analyze a news or news article only with its URL.

Aylien's power was used for this application, for more information [here.](https://docs.aylien.com/)

## Prerequisites

- Python 3.7
- Account on [Aylien.](https://docs.aylien.com/)

## RUN

    $ pip install virtualenv
    $ mkdir virtualenv
    $ cd virtualenv
    $ virtualenv webnlp

Clone this repo

    $ git clone https://github.com/jdsuarezj/wj_developerchallenge.git

Activate the virtual env

    $ source ../virtualenv/webnlp/bin/activate

Install the requirements

    $ pip install -r requirements.txt

Create fake tables for user admin

    $ python manage.py makemigrations
    $ python manage.py migrate

Config the API's credentials. Go to \app\views.py and change "ID" and "KEY" fields for yours.

Start the aplication on default port 8000

    $ python manage.py runserver

Go to "http://127.0.0.1:8000/" and enjoy!
