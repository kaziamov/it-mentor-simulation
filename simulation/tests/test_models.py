from unittest import TestCase

from simulation import models


class MapControlTestCase(TestCase):
    def setUp(self):
        self.map = models.Map()

    def test_creation_and_killing_creature(self):
        creature1 = models.Herbivore(1)
        creature2 = models.Predator(2, 1)

        self.assertEqual(len(self.map.creatures), 0)

        self.map.add_creature(creature1)
        self.assertEqual(len(self.map.creatures), 1)

        self.map.add_creature(creature1)
        self.assertEqual(len(self.map.creatures), 1)

        self.map.add_creature(creature2)
        self.assertEqual(len(self.map.creatures), 2)

        self.map.kill_creature(creature1)
        self.assertEqual(len(self.map.creatures), 1)
        self.assertTrue(creature2 in self.map.creatures)
