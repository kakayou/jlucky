import unittest
import numpy as np
import Levenshtein

class AnalyzeTestCase(unittest.TestCase):
    def test_avg(self):
        list= [x+1 for x in range(33)]
        print(np.mean(list))

    def test_split(self):
        txt = "Google#Runoob#Taobao#Facebook"
        x = txt.split("#")
        print(x)

    def test_levneshtein(self):
        str1 = "2	14	15	16	32	33"
        str2 = "2	8	13	29	32	33"
        str3 = "3	6	8	11	19	28"
        str4 = "4	9	17	20	32	33"
        str5 = "1	7	9	12	18	22"
        str6 = "12	14	18	23	30	32"

        print(Levenshtein.distance(str1,str2))
        print(Levenshtein.distance(str2, str3))
        print(Levenshtein.distance(str3, str4))
        print(Levenshtein.distance(str4, str5))
        print(Levenshtein.distance(str5, str6))


    def test_for(self):
        for i in range(2):
           print(i)
if __name__ == '__main__':
    unittest.main()
