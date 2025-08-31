# tested program:
# my_list = []
# def add(a):
#     return a + 5
#
# def stringo(s):
#     return s + 'ninanana'
#
# def container(l):
#     return my_list.append(l)
#
# def divide(a, b):
#     if b == 0:
#         return ValueError("Cannot divide by zero")
#     return a / b






import unittest
import Course_exercises
from Course_exercises import my_list


# class Test(unittest.TestCase):
#     def test1(self):
#         test_num = 20
#         result = Course_exercises.do_stuff(test_num)
#         self.assertEqual(result,25)
#     def test2(self):
#         test_num2 = 'napis'
#         result2 = Course_exercises.do_stuff(test_num2)
#         self.assertTrue(isinstance(result2, TypeError))
#     def test3(self):
#         test_num3 = None
#         result = Course_exercises.do_stuff(test_num3)
#         self.assertIsInstance(result, TypeError)
#
# if __name__ == '__main__':
#     unittest.main()

class Test(unittest.TestCase):
    def test1(self):
        param1 = 10
        result = Course_exercises.add(param1)
        self.assertEqual(result, 15)
    def test2(self):
        print('ok now running test2')
        param2 = 's'
        result2 = Course_exercises.stringo(param2)
        self.assertEqual(result2, 'sninanana')
    def test3(self):
        param3 = 7
        result3 = Course_exercises.container(param3)
        self.assertIn(param3, my_list)
    def test4(self):
        param4 = 4
        param42 = 0
        result4 = Course_exercises.divide(param4, param42)
        self.assertIsInstance(result4, ValueError)
    def tearDown(self):
        print('test completed')


if __name__ == '__main__':
    unittest.main()

















