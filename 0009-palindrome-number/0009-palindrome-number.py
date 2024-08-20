class Solution(object):
    def isPalindrome(self, x):
        
        str_x = str(x)

        reverse_str = ""

        for char in str_x:
            reverse_str = char + reverse_str

        return reverse_str == str_x

        
        