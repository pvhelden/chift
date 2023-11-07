import xmlrpc.client

URL = 'https://chift.odoo.com/'
DB = 'chift'
USER = 'philemon.vanhelden@gmx.com'
PASS = 'N$!r9FwNzD67%i'


def get_uid():
    """
    Log in to the Chift Odoo database and retrieve the user ID.

    :return: The user ID associated with the provided credentials.
    """
    uid = xmlrpc.client.ServerProxy(f'{URL}xmlrpc/common').login(DB, USER, PASS)
    return uid


def get_all_contacts(uid):
    """
    Retrieve all contacts from the Chift Odoo database.

    :param uid: The user ID for authentication.
    :return: A list of contact records fetched from the Odoo database.
    """
    models = xmlrpc.client.ServerProxy(f'{URL}/xmlrpc/2/object')
    contacts = models.execute_kw(DB, uid, PASS, 'res.partner', 'search_read', [[]], {'fields': ['name']})
    return contacts
