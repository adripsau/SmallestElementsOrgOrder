import unittest
from SmallestElement import first_n_smallest


class FindPairsTest(unittest.TestCase):

    def test_should_skip_search(self):
        self.assertEqual([], first_n_smallest([1, 2, 3, 4, 5], 0))

    def test_should_give_one_number(self):
        self.assertEqual([1], first_n_smallest([1], 1))

    def test_should_give_first_number(self):
        self.assertEqual([1], first_n_smallest([1, 2], 1))

    def test_should_find_second_number(self):
        self.assertEqual([1], first_n_smallest([2, 1], 1))

    def test_should_give_two_numbers(self):
        self.assertEqual([1, 1], first_n_smallest([1, 1, 1, 1], 2))

    def test_should_give_smallest_numbers(self):
        self.assertEqual([1, 1], first_n_smallest([4, 1, 2, 1], 2))

    def test_should_work_with_bigger_numbers(self):
        self.assertEqual([6, 2, -10, -9], first_n_smallest([6, 9, 2, -10, -9], 4))

    def test_should_work_with_duplicates(self):
        self.assertEqual([4, 2, -8, 2, -2, 0, -1, -9, -4, 2, -6, -7, 2, -5], first_n_smallest([6, 4, 2, -8, 2, -2, 8, 5, 0, 6, -1, 4, 10, -9, 7, -4, 2, -6, -7, 2, -5], 14))


if __name__ == '__main__':
    unittest.main()