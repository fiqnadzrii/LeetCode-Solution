class Solution(object):
    def longestCommonPrefix(self, strs):

        common_str = ""

        for i in range(len(strs[0])):
            for char in strs:
                if i == len(char) or char[i] != strs[0][i]:
                    return common_str
            common_str += strs[0][i]
        return common_str
        