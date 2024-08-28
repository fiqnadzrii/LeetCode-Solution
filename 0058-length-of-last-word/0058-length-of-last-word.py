class Solution(object):
    def lengthOfLastWord(self, s):

        count = 0
        s = s.rstrip()

        for char in reversed(s):
            if char == ' ':
                break
            else:
                count +=1
        return count

        