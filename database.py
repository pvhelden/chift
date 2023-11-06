import psycopg2


def get_connection():
    """
    Creates a local database connection object and returns it.

    :return: psycopg2 connection object
    """
    conn = psycopg2.connect('dbname=chift-db user=pvhelden password=admin')
    return conn


def get_all_contacts(cursor):
    """
    Fetches all contacts from the local database.

    :param cursor: psycopg2 cursor object
    :return: list of contacts
    """
    cursor.execute(f"SELECT * FROM contact;")
    contacts = cursor.fetchall()
    return contacts
