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
