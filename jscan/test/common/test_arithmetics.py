import unittest
import psutil
import time

class ArithmeticsTestCase(unittest.TestCase):

    def test_odd_Rate(self):
        process=psutil.process_iter()
        for p in process:
            print(p.name(), p.pid,p.cpu_percent())
    def test_sum(self):
        test_value = (147 / 10)
        print(test_value)

if __name__ == '__main__':
    unittest.main()
