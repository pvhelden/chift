# Chift Exercice

## Instructions

- Créer un script qui va tourner toutes les X minutes (cron) pour récupérer les contacts depuis Odoo et qui va insérer /
  mettre à jour / supprimer le(s) contact(s) dans une table dans une base de donnée de ton choix.
- Créer une interface API (de ton choix: flask, django, fastapi) qui permet de récupérer les contacts depuis la base de
  donnée directement (get contacts et get one contact by id).

## Requirements

- A PostgreSQL database created using instructions in the `database-creation.sql` file.
- Python libraries listed in the `requirements.txt` file.

## Implementation

### Cron

The `cron.py` file contains a scheduler updating the database every 15 minutes.
To run it, simply use `python ./cron.py` in a terminal.

### Database

Parameters should be stored in a `.env` file.
Uses a PostgreSQL database, which is accessed using the `psycopg2` Python library.

### Odoo

Parameters should be stored in a `.env` file.
Connects to the Chift Odoo database using the `xmlrpc` Python library.

### FastAPI

Run the server using ` uvicorn main:chift --reload`, then connect to `http://127.0.0.1:8000/docs`.
