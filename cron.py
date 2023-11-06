import time

import database
import odoo
import utils
import schedule


def update_contacts():
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
