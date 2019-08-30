import unittest

class SimpleTest1(unittest.TestCase):
    '''This is docstring for SimpleTest clazz - our unit test example'''
    def test1(self):
        '''This is docstring for test1 method'''
        v = 1 +1

class SimpleTest2(unittest.TestCase):

    def test2(self):
        '''test2 method'''
        self.assertEqual(1,2,"Its OK. I'm should fail, due 1 != 2")

    def test3(self):
        '''test3 method'''
        assert 2 == 4

if __name__ == '__main__':
    unittest.main()