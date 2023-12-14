import unittest
import sys
sys.path.append("..")
import Panda

class TestPanda(unittest.TestCase):
    def test_panda_is_created(self):
        p= Panda("Kilo,15")
        self.assertIsInstance(p,Panda)

    def test_age_is_positive(self):
        p= Panda("Kilo,15")
        self.assertGreater(p.age,0)

if __name__=='__main__':
    unittest.main()

