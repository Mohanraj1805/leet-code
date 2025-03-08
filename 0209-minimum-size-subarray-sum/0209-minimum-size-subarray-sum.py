class Solution(object):
    def minSubArrayLen(self, target, nums):
       
        l=0
        r=0
        subsum=0
        min_arr=[]
        while r<len(nums):
            subsum+=nums[r]
            while subsum>=target:
                min_arr.append(r-l+1)
                subsum-=nums[l]
                l+=1
            r+=1
        return 0 if len(min_arr)==0 else min(min_arr)

