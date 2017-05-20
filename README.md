# pdbdrop

pdb2movie web GUI

### developing

To develop, clone this repository, create a virtualenv and install the requirements:

```
git clone git@github.com:lucianoratamero/pdbdrop.git
virtualenv pdbdrop
cd pdbdrop
source bin/activate
sudo apt install libpq-dev python-dev
pip install -r requirements.txt
```

To run locally, run the database migrations:

```
python manage.py migrate
python manage.py runserver
```