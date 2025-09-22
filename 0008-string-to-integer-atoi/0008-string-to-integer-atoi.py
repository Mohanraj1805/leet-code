class Solution:
    def myAtoi(self, s: str) -> int:
        s=s.strip(' ')
        if not s:
            return 0

        minus=1
        i=0
        if s[0]=='-':
            minus=-1
            i=1

        elif s[0]=='+':
            i=1

        ans=''
        while i < len(s) and s[i].isdigit():
            ans+=s[i]
            i+=1
        if not ans:
            return 0
        res=minus*int(ans)
        int_min,int_max=-2**31,2**31-1
        if res<int_min:
            return int_min
        if res>int_max:
            return int_max
        else:
            return res