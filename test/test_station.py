import sys,unittest
sys.path.append('E:\\python\\STSimulator\\src')
from station import Station


class TestStation(unittest.TestCase):
    def setUp(self) -> None:
        self.test_station_instance = Station()
    def test_station_score_int(self):
        self.assertEqual(type(self.test_station_instance.score),int)
    def test_station_score(self):
        self.assertEqual(self.test_station_instance.score ,30)
    def test_crew_cap_int(self):
        self.assertEqual(type(self.test_station_instance.crew_cap),int)
    def test_crew_cap(self):
        self.assertEqual(self.test_station_instance.crew_cap,6)
    def test_crew_int(self):
        self.assertEqual(type(self.test_station_instance.crew_num),int)
    def test_crew_num(self):
        self.assertEqual(self.test_station_instance.crew_num,0)
    def test_str(self):
        self.assertEqual(str(self.test_station_instance),'This is a generic station.')
    def test_repr(self):
        self.assertEqual(repr(self.test_station_instance),'station score: 30, crew: 0')


if __name__ == '__main__':
    unittest.main()
