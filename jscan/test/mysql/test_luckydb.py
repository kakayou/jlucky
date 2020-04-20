import mysql.luckydb as db
import unittest


class TestLuckyDBMethod(unittest.TestCase):
    "每个测试类继承于unittest.testcase"

    def test_t_facility_group_term(self):
        s = db.t_facility_group_term()
        print(s[0][1])
        self.assertEqual(len(s), 16)

    def test_t_facility_max_term(self):
        s = db.t_facility_max_term()
        self.assertAlmostEqual(s[0], 20013)

    def test_t_query_by_SQL(self):
        s = db.t_query_by_SQL("")
        self.assertAlmostEqual(s[0], 20013)

    def test_t_facility_reds(self):
        s= db.t_facility_reds()
        print(s)
# 使本py文件可以直接$ python test.py执行测试
if __name__ == '__main__':
    unittest.main()
