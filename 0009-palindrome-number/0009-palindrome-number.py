class Solution:
    def isPalindrome(self, x: int) -> bool:
        xcopy=x
        ans=0
        if x<0:
            return False

        while x!=0:
            r=x%10
            ans=ans*10+r
            x//=10

        return True if xcopy == ans  else False