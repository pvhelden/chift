import os
import xmlrpc.client

from dotenv import load_dotenv

load_dotenv()

ODOO_URL = os.getenv('ODOO_URL')
ODOO_DB = os.getenv('ODOO_DB')
ODOO_USER = os.getenv('ODOO_USER')
ODOO_PASS = os.getenv('ODOO_PASS')


def get_uid():
    """
    Log in to the Chift Odoo database and retrieve the user ID.

    :return: The user ID associated with the provided credentials.
    """
    uid = xmlrpc.client.ServerProxy(f'{ODOO_URL}xmlrpc/common').login(ODOO_DB, ODOO_USER, ODOO_PASS)
    return uid


def get_all_contacts(uid):
    """
    Retrieve all contacts from the Chift Odoo database.

    :param uid: The user ID for authentication.
    :return: A list of contact records fetched from the Odoo database.
    """
    models = xmlrpc.client.ServerProxy(f'{ODOO_URL}/xmlrpc/2/object')
    contacts = models.execute_kw(ODOO_DB, uid, ODOO_PASS, 'res.partner', 'search_read', [[]], {'fields': ['name']})
    return contacts
