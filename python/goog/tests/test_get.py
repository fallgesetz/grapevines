import unittest
import goog.get
import goog.params

class TestGetter(unittest.TestCase):
    def test_stupid(self):
        params = goog.params.SmartParams('fb')
        getter = goog.get.Getter(params)
        print getter.header

