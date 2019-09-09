import unittest
import requests


class MyTestCase(unittest.TestCase):
    def test_case_001(self):

        url="http://www.baidu.com"
        target=requests.get(url)
        print (target.text)
        # self.assertEqual(True, False)


if __name__ == '__main__':
    unittest.main()
