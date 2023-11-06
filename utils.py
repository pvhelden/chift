def convert_from_database(old_contacts):
    """
    Unifies a list of contacts in the form [int, str] into a dictionary matching 'id' to 'name'.

    :param old_contacts: list of contacts in the form [int, str]
    :return: dictionary matching 'id' to 'name'
    """
    old_contacts = {old_contact[0]: old_contact[1] for old_contact in old_contacts}
    return old_contacts


def convert_from_odoo(contacts):
    """
    Unifies a list of contacts in the form {'id': int, 'name': str} into a dictionary matching 'id' to 'name'.

    :param contacts: list of contacts in the form {'id': int, 'name': str}
    :return: dictionary matching 'id' to 'name'
    """
    contacts = {contact['id']: contact['name'] for contact in contacts}
    return contacts


def check_name(name):
    """
    Verifies if a name is a string and adds a quotation mark in front of existing ones to prepare for SQL.

    :param name: name to check
    :return: updated name
    """
    if not isinstance(name, str):
        name = ''
    elif "'" in name:
        name = name.replace("'", "''")
    return name
