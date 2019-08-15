# encoding:utf-8
# 开发团队：SDET_05
# 开发人员：渣渣灰
# 开发时间： 2019/7/19   14:56
# 文件名称： test_tice_716.py
# 开发工具： PyCharm
import  unittest
from tice_716 import Yunsuan

class TestTice716(unittest.TestCase):
    def test_yunsuan(self):
        pop=Yunsuan()
        self.assertEqual(pop.jia(1,2),3)
        self.assertEqual(pop.jia(-1,-2),-3)
        self.assertEqual(pop.jia(-1,1.5),0.5)
        self.assertEqual(pop.plus(2,3),6)
        self.assertEqual(pop.plus(-1,-4),4)



if __name__=="__main__":
    unittest.main()
