def convert_from_database(old_contacts):
    """
    Convert a list of contacts in the format [int, str] into a dictionary matching 'id' to 'name'.

    :param old_contacts: A list of contacts in the format [int, str].
    :return: A dictionary matching 'id' to 'name'.
    """
    old_contacts = {old_contact[0]: old_contact[1] for old_contact in old_contacts}
    return old_contacts


def convert_from_odoo(contacts):
    """
    Convert a list of contacts in the format {'id': int, 'name': str} into a dictionary matching 'id' to 'name'.

    :param contacts: A list of contacts in the format {'id': int, 'name': str}.
    :return: A dictionary matching 'id' to 'name'.
    """
    contacts = {contact['id']: contact['name'] for contact in contacts}
    return contacts


def check_name(name):
    """
    Verify if a name is a string and escape single quotation marks for SQL compatibility.

    :param name: The name to check.
    :return: An updated name with single quotation marks escaped.
    """
    if not isinstance(name, str):
        name = ''
    elif "'" in name:
        name = name.replace("'", "''")
    return name
