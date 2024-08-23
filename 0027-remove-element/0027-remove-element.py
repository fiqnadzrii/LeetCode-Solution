class Solution(object):
    def removeElement(self, nums, val):
        
        new_nums = []

        for num in nums:
            if num != val:
                new_nums.append(num)
        
        for i in range(len(new_nums)):
            nums[i] = new_nums[i]

        return len(new_nums)
            
        