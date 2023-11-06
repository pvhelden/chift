import xmlrpc.client

URL = 'https://chift.odoo.com/'
DB = 'chift'
USER = 'philemon.vanhelden@gmx.com'
PASS = 'N$!r9FwNzD67%i'


def get_uid():
    """
    Logs in to the Chift Odoo database, and fetches the user id.

    :return: user id
    """
    uid = xmlrpc.client.ServerProxy(f'{URL}xmlrpc/common').login(DB, USER, PASS)
    return uid


def get_all_contacts(uid):
    """
    Fetches all contacts from the Chift Odoo database.

    :param uid: user id
    :return: list of contacts
    """
    models = xmlrpc.client.ServerProxy(f'{URL}/xmlrpc/2/object')
    contacts = models.execute_kw(DB, uid, PASS, 'res.partner', 'search_read', [[]], {'fields': ['name']})
    return contacts
