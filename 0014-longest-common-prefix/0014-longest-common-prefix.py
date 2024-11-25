class Solution(object):
    def longestCommonPrefix(self, strs):
        if not strs:
            return ""
        
        char = ''
        for i in range(0, min(len(s) for s in strs)):  # Get the shortest string length
            if all(s[i] == strs[0][i] for s in strs):  # Check if all strings have 
                char += strs[0][i]
            else:
                break
        
        return char
