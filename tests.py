import unittest

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


if __name__ == '__main__':
    unittest.main()
