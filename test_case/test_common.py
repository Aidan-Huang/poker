from common import Common


class TestCommonMethods:

    def test_is_contain_sub_list(self):
        big_list = [10, 4, 3, 2]
        sub_list = [2, 4, 3]

        assert Common.is_contain_sub_list(big_list, sub_list) is True
