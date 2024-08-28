class Solution(object):
    def plusOne(self, digits):
        
        for i in reversed(range(len(digits))):
            if digits[i] < 9:
                digits[i] +=1
                return digits
            elif digits[i] == 9:
                digits[i] = 0
        
        return [1] + digits



       