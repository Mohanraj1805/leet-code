class Solution(object):
    def isIsomorphic(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        if len(s)!=len(t):
            return False
    
        map_of_s=[]
        map_of_t=[]
        for i in s:
            map_of_s.append(s.index(i))
        for j in t:
            map_of_t.append(t.index(j))
        if map_of_s==map_of_t:
            return True
       
        return False
