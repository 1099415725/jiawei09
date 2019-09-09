import unittest
import requests


class MyTestCase(unittest.TestCase):
    def test_something(self):
        url="http://www.baidu.com"
        devices=requests.get(url)
        print (devices)

if __name__ == '__main__':
    unittest.main()
