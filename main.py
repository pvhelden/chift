import xmlrpc.client


def main():
    url = 'https://chift.odoo.com/'
    db = 'chift'
    user = 'philemon.vanhelden@gmx.com'
    password = 'N$!r9FwNzD67%i'

    uid = xmlrpc.client.ServerProxy(url + 'xmlrpc/common').login(db, user, password)


if __name__ == '__main__':
    main()
