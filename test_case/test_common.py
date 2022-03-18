import unittest
from common import Common


class TestCommonMethods(unittest.TestCase):

    def test_is_contain_sub_list(self):
        list = [10, 4, 3, 2]
        sub_list = [2, 4, 3]

        self.assertTrue(Common.is_contain_sub_list(list, sub_list))


if __name__ == '__main__':
    unittest.main()
