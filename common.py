class Common:

    @staticmethod
    def is_contain_sub_list(origin_list, sub_list):
        if all(x in origin_list for x in sub_list):
            return True

        return False
