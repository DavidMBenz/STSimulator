import sys,unittest
sys.path.append('E:\\python\\STSimulator\\src')
from starship import Starship

class TestStarship(unittest.TestCase):
    def setUp(self) -> None:
        self.test_starship_instance = Starship('test')
    def test_name_str(self):
        self.assertTrue(type(self.test_starship_instance.name) == str)
    def test_powerlevel(self):
        self.assertEqual(self.test_starship_instance.power_level,1000)
    def test_power_min(self):
        self.assertEqual(self.test_starship_instance.power_min, 0)
    def test_power_max(self):
        self.assertEqual(self.test_starship_instance.power_max, 1000)
    def test_population(self):
        self.assertEqual(self.test_starship_instance.population,0)
    def test_population_int(self):
        self.assertTrue(type(self.test_starship_instance.population)==int)
    def test_population_min(self):
        self.assertEqual(self.test_starship_instance.population_min,0)
    def test_population_max(self):
        self.assertEqual(self.test_starship_instance.population_max,30)
    def test_shield_min(self):
        self.assertEqual(self.test_starship_instance.shield_min, 0)
    def test_shield_max(self):
        self.assertEqual(self.test_starship_instance.shield_max, 100)
    def test_shield_int(self):
        self.assertTrue(type(self.test_starship_instance.shield) == int)
    def test_shield(self):
        self.assertEqual(self.test_starship_instance.shield, 100)
    def test_str(self):
        self.assertEqual(str(self.test_starship_instance),'This is the starship "test".')
    def test_repr(self):
        self.assertEqual(repr(self.test_starship_instance),'starship name: test, power: 1000, shield: 100, pop: 0')
    #def test_something(self):
        #self.assertEqual(True, False)


if __name__ == '__main__':
    unittest.main()
