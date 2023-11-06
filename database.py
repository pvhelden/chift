import psycopg2

import utils


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


def get_contact_by_id(cursor, contact_id):
    """
    Fetches a specific contact from the local database using given id.

    :param cursor: psycopg2 cursor object
    :param contact_id: psycopg2 cursor object
    :return: contact infox
    """
    cursor.execute(f"SELECT * FROM contact WHERE id={contact_id};")
    contact = cursor.fetchone()
    return contact


def update_contacts(cursor, old_contacts, contacts):
    """
    Replaces old contacts in the local database from contacts in the Chift Odoo database.

    :param cursor: psycopg2 cursor object
    :param old_contacts: list of old contacts from the local database
    :param contacts: list of contacts from the Chift Odoo database
    :return: None
    """
    # Delete obsolete contacts from local database
    delete_ids = old_contacts.keys() - contacts.keys()
    for old_contact_id in delete_ids:
        cursor.execute(f"DELETE FROM contact WHERE id={old_contact_id};")
    print(f"Deleted {len(delete_ids)} obsolete contacts from local database.")

    # Add/update contacts from Chift Odoo database
    for contact_id, contact_name in contacts.items():
        name = utils.check_name(contact_name)
        if contact_id in old_contacts:
            # Update existing contact
            if contact_name != old_contacts[contact_id]:
                cursor.execute(f"UPDATE contact SET name='{name}' WHERE id={contact_id};")
        else:
            # Add new contact
            cursor.execute(f"INSERT INTO contact VALUES({contact_id}, '{name}')")
    print(f"Added/updated {len(contacts)} contacts in local database.")
