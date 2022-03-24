class Common:

    @staticmethod
    # 判断数组是否包含另一个数组
    def is_contain_sub_list(origin_list, sub_list):
        if all(x in origin_list for x in sub_list):
            return True

        return False

    @staticmethod
    # 在数组中寻找重复指定次数的值
    # 参数：nums 数组， times 指定次数
    # 返回：所有符合条件的值数组
    def find_repeat(nums, times):
        result = []
        f_find = True
        index = 0
        # i 指针
        for i in range(len(nums) - (times - 1)):
            if i < index:
                continue
            else:
                number = nums[i]
                # 往前比较 重复次数减1 次
                for time in range(1, times):
                    if number != nums[i + time]:
                        f_find = False
                        break
                if f_find:
                    result.append(number)
                    index += times - 1
                f_find = True

                index += 1

        return result

    @staticmethod
    def remove_repeat(nums):
        if not nums:
            return []

        result = []

        for n in nums:
            if n not in result:
                result.append(n)

        return result


class Test:

    def test(self):
        for i in range(5):
            print(i)

