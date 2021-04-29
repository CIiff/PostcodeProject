from .post_code import PostCode
import unittest


class PostcodeTests(unittest.TestCase):

    pc = PostCode("SE12 0NB")

    def test_country(self):
        self.assertIs(type(self.pc.country()), str)
        self.assertEqual(self.pc.country(), "England")

    def test_admin_district(self):
        self.assertIs(type(self.pc.admin_district()), str)
        self.assertEqual(self.pc.admin_district(), "Lewisham")

    def test_admin_ward(self):
        self.assertIs(type(self.pc.admin_ward()), str)
        self.assertEqual(self.pc.admin_ward(), "Grove Park")

    def test_region(self):
        self.assertIs(type(self.pc.region()), str)
        self.assertEqual(self.pc.region(), "London")

    def test_postcode(self):
        self.assertIs(type(self.pc.postcode()), str)
        self.assertEqual(self.pc.postcode(), "SE12 0NB")
