class Solution(object):
    def mergeAlternately(self, word1, word2):
        """
        :type word1: str
        :type word2: str
        :rtype: str
        """
        ans=''
        if len(word1)<len(word2):
            for i in range(len(word1)):
                ans+=word1[i]+word2[i]
            return(ans+word2[len(word1):])
        else:
            for i in range(len(word2)):
                ans+=word1[i]+word2[i]
            return(ans+word1[len(word2):])