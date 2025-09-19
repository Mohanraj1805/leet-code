class Solution:
    def singleNonDuplicate(self, nums: List[int]) -> int:
        #Binary search 
     
        l=0
        r=len(nums)-1
        while l <= r:
            m=(l+r)//2
            if(m-1<0 or nums[m-1]!=nums[m]) and (m+1==len(nums)or nums[m+1]!=nums[m]):
                return nums[m]
            leftside = m-1 if nums[m-1]==nums[m] else m
            if leftside%2==1:
                r=m-1
            else:
                l=m+1
        



        # res={}
        # for i in nums:
        #     if i  in res:
        #         res[i]+=1
        #     else:
        #         res[i]=1
        # for r in res:

        #     if res[r]==1:
        #         return r
