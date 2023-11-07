import time

import schedule

import database
import odoo
import utils


def update_contacts():
    """
    Update the local contacts database by synchronizing it with Odoo contacts.

    This function performs the following steps:
    1. Retrieves the existing local contacts from the database.
    2. Retrieves Odoo contacts.
    3. Converts the contacts from both sources into a common format.
    4. Updates the local database with the new contacts.

    Note: The function is intended to be scheduled to run at regular intervals.

    :return: None
    """
    # Get local contacts
    conn = database.get_connection()
    cursor = conn.cursor()
    old_contacts = database.get_all_contacts(cursor)
    old_contacts = utils.convert_from_database(old_contacts)

    # Get Odoo contacts
    uid = odoo.get_uid()
    contacts = odoo.get_all_contacts(uid)
    contacts = utils.convert_from_odoo(contacts)

    # Update local database then close connection
    database.update_contacts(cursor, old_contacts, contacts)
    try:
        conn.commit()
        cursor.close()
    except Exception as e:
        conn.rollback()
        print(f"Error: {e}")


if __name__ == '__main__':
    schedule.every(15).minutes.do(update_contacts)

    while True:
        schedule.run_pending()
        time.sleep(1)
