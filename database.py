import psycopg2

import utils


def get_connection():
    """
    Establish a connection to the local PostgreSQL database and return the connection object.

    :return: psycopg2 connection object
    """
    conn = psycopg2.connect('dbname=chift-db user=postgres password=admin')
    return conn


def get_all_contacts(cursor):
    """
    Retrieve all contacts from the local database.

    :param cursor: psycopg2 cursor object
    :return: A list of contacts fetched from the local database.
    """
    cursor.execute(f"SELECT * FROM public.contact;")
    contacts = cursor.fetchall()
    return contacts


def get_contact_by_id(cursor, contact_id):
    """
    Retrieve a specific contact from the local database using its ID.


    :param cursor: psycopg2 cursor object
    :param contact_id: The unique ID of the contact to fetch.
    :return: Information about the contact as a tuple, or None if not found.
    """
    cursor.execute(f"SELECT * FROM public.contact WHERE id={contact_id};")
    contact = cursor.fetchone()
    return contact


def update_contacts(cursor, old_contacts, contacts):
    """
    Synchronize and update local database contacts with Chift Odoo contacts.

    :param cursor: psycopg2 cursor object
    :param old_contacts: A dictionary of existing local contacts.
    :param contacts: A dictionary of Chift Odoo contacts.
    :return: None
    """
    # Delete obsolete contacts from local database
    delete_ids = old_contacts.keys() - contacts.keys()
    for old_contact_id in delete_ids:
        cursor.execute(f"DELETE FROM public.contact WHERE id={old_contact_id};")
    print(f"Deleted {len(delete_ids)} obsolete contacts from local database.")

    # Add/update contacts from Chift Odoo database
    for contact_id, contact_name in contacts.items():
        name = utils.check_name(contact_name)
        if contact_id in old_contacts:
            # Update existing contact
            if contact_name != old_contacts[contact_id]:
                cursor.execute(f"UPDATE public.contact SET name='{name}' WHERE id={contact_id};")
        else:
            # Add new contact
            cursor.execute(f"INSERT INTO public.contact VALUES({contact_id}, '{name}')")
    print(f"Added/updated {len(contacts)} contacts in local database.")
