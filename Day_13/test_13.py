import unittest

import day_13_attempt_two as d13

class Test13(unittest.TestCase):

    def test_simple_format(self):
        self.assertEqual(d13.format_input("[1]"), [1])
        self.assertEqual(d13.format_input("[1,2,3]"), [1,2,3])

    def test_nested_format(self):
        self.assertEqual(d13.format_input("[[1]]"), [[1]])
        self.assertEqual(d13.format_input("[[[1]]]"), [[[1]]])

    def test_complext_format(self):
        self.assertEqual(d13.format_input("[[1,2],3,[4,[5]]]"), [[1,2],3,[4,[5]]])

    def test_compare_non_destructive(self):
        lst = [1, [2]]
        self.assertEqual(d13.compare_lists(lst, [1, [1]]), False)
        self.assertEqual(lst, [1, [2]])
