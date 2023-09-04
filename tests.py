import unittest

from packages_to_load import which_packages_to_load


class TestPackagesToLoad(unittest.TestCase):
    def test_full_1(self):
        actual = which_packages_to_load(110, [20, 70, 90, 30, 60, 110])
        expected = [20, 60]
        self.assertEqual(actual, expected)

    def test_full_2(self):
        actual = which_packages_to_load(130, [90, 80, 30, 20, 9, 19])
        expected = [20, 80]
        self.assertEqual(actual, expected)

    def test_not_full(self):
        actual = which_packages_to_load(110, [18, 70, 90, 30, 58, 110])
        expected = [18, 58]
        self.assertEqual(actual, expected)

    def test_full_truck(self):
        actual = which_packages_to_load(20, [1, 2])
        expected = []
        self.assertEqual(actual, expected)

    def test_one_package_in_storage(self):
        actual = which_packages_to_load(100, [1])
        expected = []
        self.assertEqual(actual, expected)

    def test_empty_storage(self):
        actual = which_packages_to_load(100, [])
        expected = []
        self.assertEqual(actual, expected)

    def test_packages_biggest_truck_space(self):
        actual = which_packages_to_load(50, [60, 70, 90, 100, 110, 120])
        expected = []
        self.assertEqual(actual, expected)
