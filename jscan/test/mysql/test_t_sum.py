import mysql.t_sum as db
import unittest


class Test_t_sum(unittest.TestCase):
    "每个测试类继承于unittest.testcase"
    def test_t_sum_insert(self):
        data = list()
        data.append((1,1))
        s = db.t_sum_insert(data)
    def test_t_sum_clear(self):
        inspectionItems = [{"category": "system", "subtype": "disk", "signID": ""}]
        for item in inspectionItems:

            print(item['subtype'])

# 使本py文件可以直接$ python test.py执行测试
if __name__ == '__main__':
    unittest.main()
