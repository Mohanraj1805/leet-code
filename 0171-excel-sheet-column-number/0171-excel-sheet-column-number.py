class Solution(object):
    def titleToNumber(self, columnTitle):
        """
        :type columnTitle: str
        :rtype: int
        """
        count=0
        for i in columnTitle:
            ans=ord(i)-ord('A')+1
            count=count*26+ ans
        return count