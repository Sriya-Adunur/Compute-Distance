# Tests a type representing one-way roads connecting cities.
# CSC 101, Project 5
# Given tests, Winter '23

import unittest
import city
import road


class TestRoad(unittest.TestCase):
    def test01_init(self):
        sfo = city.City("San Francisco")
        sbp = city.City("San Luis Obispo")

        road_a = road.Road(sfo, sbp, 232)

        self.assertIs(road_a.start, sfo)
        self.assertIs(road_a.end, sbp)
        self.assertEqual(road_a.distance, 232)
        self.assertEqual(sfo.roads, {"San Luis Obispo": road_a})
        self.assertEqual(sbp.roads, {})

    def test02_init(self):
        sfo = city.City("San Francisco")
        sbp = city.City("San Luis Obispo")
        lax = city.City("Los Angeles")

        road_a = road.Road(sfo, sbp, 232)
        road_b = road.Road(sfo, lax, 381)
        road_c = road.Road(sbp, lax, 189)

        self.assertIs(road_a.start, sfo)
        self.assertIs(road_a.end, sbp)
        self.assertEqual(road_a.distance, 232)
        self.assertIs(road_b.start, sfo)
        self.assertIs(road_b.end, lax)
        self.assertEqual(road_b.distance, 381)
        self.assertIs(road_c.start, sbp)
        self.assertIs(road_c.end, lax)
        self.assertEqual(road_c.distance, 189)
        self.assertIs(sfo.roads[sbp.name], road_a)
        self.assertIs(sfo.roads[lax.name], road_b)
        self.assertIs(sbp.roads[lax.name], road_c)

    def test03_eq(self):
        sfo = city.City("San Francisco")
        sbp = city.City("San Luis Obispo")

        road_a = road.Road(sfo, sbp, 232)
        road_b = road.Road(sfo, sbp, 232)

        self.assertEqual(road_a, road_a)
        self.assertEqual(road_a, road_b)

    def test04_eq(self):
        sfo = city.City("San Francisco")
        sbp = city.City("San Luis Obispo")
        lax = city.City("Los Angeles")

        road_a = road.Road(sfo, sbp, 232)
        road_b = road.Road(sbp, sfo, 232)
        road_c = road.Road(sfo, lax, 381)
        road_d = road.Road(lax, sfo, 381)
        road_e = road.Road(sbp, lax, 189)
        road_f = road.Road(lax, sbp, 189)

        self.assertEqual(road_a, road_a)
        self.assertNotEqual(road_a, road_b)
        self.assertNotEqual(road_a, road_c)
        self.assertNotEqual(road_a, road_d)
        self.assertNotEqual(road_a, road_e)
        self.assertNotEqual(road_a, road_f)
        self.assertNotEqual(road_c, road_a)
        self.assertNotEqual(road_c, road_b)
        self.assertEqual(road_c, road_c)
        self.assertNotEqual(road_c, road_d)
        self.assertNotEqual(road_c, road_e)
        self.assertNotEqual(road_c, road_f)
        self.assertNotEqual(road_e, road_a)
        self.assertNotEqual(road_e, road_b)
        self.assertNotEqual(road_e, road_c)
        self.assertNotEqual(road_e, road_d)
        self.assertEqual(road_e, road_e)
        self.assertNotEqual(road_e, road_f)

    def test05_repr(self):
        sfo = city.City("San Francisco")
        sbp = city.City("San Luis Obispo")

        road_a = road.Road(sfo, sbp, 232)

        self.assertEqual(str(road_a), "San Francisco to San Luis Obispo (232)")

    def test06_repr(self):
        sfo = city.City("San Francisco")
        sbp = city.City("San Luis Obispo")
        lax = city.City("Los Angeles")

        road_a = road.Road(sfo, sbp, 232)
        road_b = road.Road(sbp, sfo, 232)
        road_c = road.Road(sfo, lax, 381)
        road_d = road.Road(lax, sfo, 381)
        road_e = road.Road(sbp, lax, 189)
        road_f = road.Road(lax, sbp, 189)

        self.assertEqual(str(road_a), "San Francisco to San Luis Obispo (232)")
        self.assertEqual(str(road_b), "San Luis Obispo to San Francisco (232)")
        self.assertEqual(str(road_c), "San Francisco to Los Angeles (381)")
        self.assertEqual(str(road_d), "Los Angeles to San Francisco (381)")
        self.assertEqual(str(road_e), "San Luis Obispo to Los Angeles (189)")
        self.assertEqual(str(road_f), "Los Angeles to San Luis Obispo (189)")


if __name__ == "__main__":
    unittest.main()
