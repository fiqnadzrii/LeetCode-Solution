class Solution(object):
    def findDisappearedNumbers(self, nums):

        n = len(nums)
        nums = sorted(set(nums))
        missing_num = []
        expected = 1

        for num in nums:
            while expected < num:
                missing_num.append(expected)
                expected += 1
            expected += 1

        while expected <= n:
            missing_num.append(expected)
            expected +=1

        return missing_num

        