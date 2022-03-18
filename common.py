class Common:

    @staticmethod
    def is_contain_sub_list(list, sub_list):
        if all(x in list for x in sub_list):
            return True

        return False
