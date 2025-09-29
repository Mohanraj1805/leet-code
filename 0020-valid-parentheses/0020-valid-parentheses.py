class Solution:
    def isValid(self, s: str) -> bool:
        res=[]
        for i in s:
            if i =='(':
                res.append(')')
            elif i =='[':
                res.append(']')
            elif i == '{':
                res.append("}")
            elif not res or res.pop() != i:
                return False
        return not res