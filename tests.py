import unittest

import psycopg2.extensions

import database
import odoo
import utils


class TestOdoo(unittest.TestCase):
    uid = None

    @classmethod
    def setUpClass(cls):
        cls.uid = odoo.get_uid()

    def test_get_uid(self):
        self.assertIsInstance(self.uid, int)

    def test_get_all_contacts(self):
        contacts = odoo.get_all_contacts(self.uid)
        self.assertIsInstance(contacts, list)


class TestDatabase(unittest.TestCase):
    cursor = None
    conn = None

    @classmethod
    def setUpClass(cls):
        cls.conn = database.get_connection()
        cls.cursor = cls.conn.cursor()

    @classmethod
    def tearDownClass(cls):
        cls.cursor.close()

    def test_get_conn(self):
        conn = database.get_connection()
        self.assertIsInstance(conn, psycopg2.extensions.connection)

    def test_get_all_contacts(self):
        contacts = database.get_all_contacts(self.cursor)
        self.assertIsInstance(contacts, list)

    def test_update_contacts(self):
        # Get local contacts
        old_contacts = database.get_all_contacts(self.cursor)
        old_contacts = utils.convert_from_database(old_contacts)

        # Get fake Odoo contacts
        contacts = [{'id': 1, 'name': 'test'}]
        contacts = utils.convert_from_odoo(contacts)

        database.update_contacts(self.cursor, old_contacts, contacts)

        new_contacts = database.get_all_contacts(self.cursor)
        self.assertEqual([(1, 'test')], new_contacts)


if __name__ == '__main__':
    unittest.main()
