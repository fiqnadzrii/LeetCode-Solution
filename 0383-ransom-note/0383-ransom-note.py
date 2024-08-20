class Solution(object):
    def canConstruct(self, ransomNote, magazine):
        """
        :type ransomNote: str
        :type magazine: str
        :rtype: bool
        """

        lettercount = {}

        for char in magazine:
            if char in lettercount:
                lettercount[char] += 1
            elif char not in lettercount:
                lettercount[char] = 1

        for char in ransomNote:
            if char in lettercount and lettercount[char] > 0:
                lettercount[char] -=1
            else:
                return False

        return True
            

        
        