import unittest
from common import Common


class TestCommonMethods(unittest.TestCase):

    def test_is_contain_sub_list(self):
        big_list = [10, 4, 3, 2]
        sub_list = [2, 4, 3]

        assert Common.is_contain_sub_list(big_list, sub_list) is True

    def test_find_repeat(self):

        nums = [1, 1, 2, 3, 3, 4, 4, 5, 6, 7, 7]
        assert Common.find_repeat(nums, 2) == [1, 3, 4, 7]
        assert Common.find_repeat(nums, 3) == []

        nums = [1, 1, 1, 2, 3, 3, 3, 4, 4, 4, 5, 6, 6, 7, 7, 7]
        assert Common.find_repeat(nums, 2) == [1, 3, 4, 6, 7]
        assert Common.find_repeat(nums, 3) == [1, 3, 4, 7]

        nums = [1, 1, 1, 2, 3, 3, 3, 4, 4, 4, 4, 5, 6, 6, 7, 7, 7]
        assert Common.find_repeat(nums, 2) == [1, 3, 4, 4, 6, 7]
        assert Common.find_repeat(nums, 4) == [4]

    def test_remove_repeat(self):

        nums = [1]
        assert Common.remove_repeat(nums) == [1]

        nums = [1, 1]
        assert Common.remove_repeat(nums) == [1]

        nums = [1, 1, 1, 2, 2]
        assert Common.remove_repeat(nums) == [1, 2]

