python-scrum
===
A minimal implementation of a scrum tool using Django.

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

Activate virtual environment

`source virutalenv/bin/activate`

Install project requirements

`pip install -r requirements.txt`


## Usage

From project root:

Activate virtual environment if not already

Debian:

`source virtualenv/bin/activate`

`cd scrum`

`python manage.py <commands>`  i.e. runserver, makemigrations, migrate

Visit `localhost:8000`

To exit virtual python environment:

`deactivate`

## License

The Unlicense; see LICENSE