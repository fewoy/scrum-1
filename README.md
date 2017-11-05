python-scrum
===
A minimal implementation of a scrum tool using Django and Material Design Lite

## Requirements
* Python 3
* pip
* virtualenv

## Installation

### Install Python 3

Debian:

`sudo apt install build-essential libssl-dev libffi-dev python3-dev python3-venv`

### Install Pip

Install [pip](https://pip.pypa.io/en/stable/installing/)

### Virtualenv

Install [Virtualenv](https://virtualenv.pypa.io/en/stable/)

### Install project environment

From project root:

Debian:

`virtualenv -p python3 virutalenv`

1. Activate virtual environment

    `source virutalenv/bin/activate`

2. Install project requirements

    `pip install -r requirements.txt`


## Usage

From project root:


Debian:

1. Activate virtual environment if not already

    `source virtualenv/bin/activate`

2. Change into app directory

    `cd scrum`

3. One-time database configuration

    3. Migrate database 

        `python manage.py makemigrations`

        `python manage.py migrate`

    3. Load seed data

        `python manage.py loaddata default.json`

4. Run server

    `python manage.py runserver`

5. Visit `localhost:8000/admin`

6. Default admin user
    * Username: admin
    * Password: admin


To exit virtual python environment:

`deactivate`

## License

The Unlicense; see LICENSE