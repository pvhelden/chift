import unittest

import psycopg2.extensions

import database
import odoo


class TestOdoo(unittest.TestCase):
    uid = None

    @classmethod
    def setUpClass(cls):
        cls.uid = odoo.get_uid()

    def test_get_uid(self):
        print(self.uid)
        self.assertIsInstance(self.uid, int)

    def test_get_all_contacts(self):
        contacts = odoo.get_all_contacts(self.uid)
        print(contacts)
        self.assertTrue(len(contacts))


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
        print(conn)
        self.assertIsInstance(conn, psycopg2.extensions.connection)

    def test_get_all_contacts(self):
        contacts = database.get_all_contacts(self.cursor)
        print(contacts)
        self.assertTrue(len(contacts))


if __name__ == '__main__':
    unittest.main()
