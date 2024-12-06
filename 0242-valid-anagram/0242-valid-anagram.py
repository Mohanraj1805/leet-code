class Solution(object):
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        if len(s)!=len(t):
            return False
        ans=set()
        for i in s:
            if i not in ans:
                ans.add(i)
                if s.count(i)!=t.count(i): return False
        return True