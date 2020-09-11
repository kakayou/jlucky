import mysql.t_facility as tf
import unittest


class TestLuckyDBMethod(unittest.TestCase):
    "每个测试类继承于unittest.testcase"

    def test_t_facility(self):
        history = tf.t_facility()
        length = len(history)
        for i in range(length):
            comp = history.pop()
            for item in history:
                if len(set.intersection(set(item[0:6]), set(comp[0:6]))) > 5:
                    print(item)


# 使本py文件可以直接$ python test.py执行测试
if __name__ == '__main__':
    unittest.main()
