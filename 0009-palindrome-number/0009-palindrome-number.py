class Solution:
    def isPalindrome(self, x: int) -> bool:
        xcopy=x
        ans=0
        flag=0
        if x<0:
            flag=1
            x*=-1
        while x!=0:
            r=x%10
            ans=ans*10+r
            x//=10

        return True if xcopy == ans  else False