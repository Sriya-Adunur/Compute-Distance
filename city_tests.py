# Tests a type representing cities connected by roads.
# CSC 101, Project 5
# Given tests, Winter '23

import unittest
import city


class TestCity(unittest.TestCase):
    def test01_init(self):
        sfo = city.City("San Francisco")

        self.assertEqual(sfo.name, "San Francisco")
        self.assertEqual(sfo.roads, {})

    def test02_eq(self):
        sfo = city.City("San Francisco")
        lax = city.City("Los Angeles")

        self.assertEqual(sfo, sfo)
        self.assertNotEqual(sfo, lax)
        self.assertNotEqual(lax, sfo)
        self.assertEqual(lax, lax)

    def test03_repr(self):
        sfo = city.City("San Francisco")

        self.assertEqual(str(sfo), "San Francisco")



if __name__ == "__main__":
    unittest.main()
