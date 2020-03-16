import sys,unittest
sys.path.append('E:\\python\\STSimulator\\src')
from stations import Command,Science,Tactical,Engineering,Medical


class TestCommand(unittest.TestCase):
    def setUp(self) -> None:
        self.test_command_instance = Command()
    def test_command_score_int(self):
        self.assertEqual(type(self.test_command_instance.score),int)
    def test_station_score(self):
        self.assertEqual(self.test_command_instance.score ,30)
    def test_crew_cap_int(self):
        self.assertEqual(type(self.test_command_instance.crew_cap),int)
    def test_crew_cap(self):
        self.assertEqual(self.test_command_instance.crew_cap,6)
    def test_crew_int(self):
        self.assertEqual(type(self.test_command_instance.crew_num),int)
    def test_crew_num(self):
        self.assertEqual(self.test_command_instance.crew_num,0)
    def test_str(self):
        self.assertEqual(str(self.test_command_instance),'This is the command station.')
    def test_repr(self):
        self.assertEqual(repr(self.test_command_instance),'command station score: 30, crew: 0')

class TestScience(unittest.TestCase):
    def setUp(self) -> None:
        self.test_science_instance = Science()
    def test_science_score_int(self):
        self.assertEqual(type(self.test_science_instance.score),int)
    def test_station_score(self):
        self.assertEqual(self.test_science_instance.score ,30)
    def test_crew_cap_int(self):
        self.assertEqual(type(self.test_science_instance.crew_cap),int)
    def test_crew_cap(self):
        self.assertEqual(self.test_science_instance.crew_cap,6)
    def test_crew_int(self):
        self.assertEqual(type(self.test_science_instance.crew_num),int)
    def test_crew_num(self):
        self.assertEqual(self.test_science_instance.crew_num,0)
    def test_str(self):
        self.assertEqual(str(self.test_science_instance),'This is the science station.')
    def test_repr(self):
        self.assertEqual(repr(self.test_science_instance),'science station score: 30, crew: 0')

class TestTactical(unittest.TestCase):
    def setUp(self) -> None:
        self.test_tactical_instance = Tactical()
    def test_tactical_score_int(self):
        self.assertEqual(type(self.test_tactical_instance.score),int)
    def test_station_score(self):
        self.assertEqual(self.test_tactical_instance.score ,30)
    def test_crew_cap_int(self):
        self.assertEqual(type(self.test_tactical_instance.crew_cap),int)
    def test_crew_cap(self):
        self.assertEqual(self.test_tactical_instance.crew_cap,6)
    def test_crew_int(self):
        self.assertEqual(type(self.test_tactical_instance.crew_num),int)
    def test_crew_num(self):
        self.assertEqual(self.test_tactical_instance.crew_num,0)
    def test_str(self):
        self.assertEqual(str(self.test_tactical_instance),'This is the tactical station.')
    def test_repr(self):
        self.assertEqual(repr(self.test_tactical_instance),'tactical station score: 30, crew: 0')
        
class TestEngineering(unittest.TestCase):
    def setUp(self) -> None:
        self.test_engineering_instance = Engineering()
    def test_engineering_score_int(self):
        self.assertEqual(type(self.test_engineering_instance.score),int)
    def test_station_score(self):
        self.assertEqual(self.test_engineering_instance.score ,30)
    def test_crew_cap_int(self):
        self.assertEqual(type(self.test_engineering_instance.crew_cap),int)
    def test_crew_cap(self):
        self.assertEqual(self.test_engineering_instance.crew_cap,6)
    def test_crew_int(self):
        self.assertEqual(type(self.test_engineering_instance.crew_num),int)
    def test_crew_num(self):
        self.assertEqual(self.test_engineering_instance.crew_num,0)
    def test_str(self):
        self.assertEqual(str(self.test_engineering_instance),'This is the engineering station.')
    def test_repr(self):
        self.assertEqual(repr(self.test_engineering_instance),'engineering station score: 30, crew: 0')

class TestMedical(unittest.TestCase):
    def setUp(self) -> None:
        self.test_medical_instance = Medical()
    def test_medical_score_int(self):
        self.assertEqual(type(self.test_medical_instance.score),int)
    def test_station_score(self):
        self.assertEqual(self.test_medical_instance.score ,30)
    def test_crew_cap_int(self):
        self.assertEqual(type(self.test_medical_instance.crew_cap),int)
    def test_crew_cap(self):
        self.assertEqual(self.test_medical_instance.crew_cap,6)
    def test_crew_int(self):
        self.assertEqual(type(self.test_medical_instance.crew_num),int)
    def test_crew_num(self):
        self.assertEqual(self.test_medical_instance.crew_num,0)
    def test_str(self):
        self.assertEqual(str(self.test_medical_instance),'This is the medical station.')
    def test_repr(self):
        self.assertEqual(repr(self.test_medical_instance),'medical station score: 30, crew: 0')


if __name__ == '__main__':
    unittest.main()
