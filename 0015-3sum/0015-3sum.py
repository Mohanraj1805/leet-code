class Solution(object):
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        res=set()
        nums.sort()
        for i , a in enumerate(nums):
            if i >0 and a==nums[i-1]:# if the value is anme continue
                continue
            l,r=i+1,len(nums)-1
            while l<r:
                threesum=  a+ nums[l]+nums[r]
                if threesum > 0:
                    r-=1
                elif threesum <0:
                    l+=1
                else:
                    res.add((a,nums[l],nums[r]))
                    l+=1
                    r-=1
        return list(res)

        # ans = set()
        
        # n = len(nums)
        # nums.sort()
        # for i in range(n):
        #     for j in range(i + 1, n):
        #         for k in range(j + 1, n):
        #             if nums[i] + nums[j] + nums[k] == 0:
        #                 ans.add((nums[i], nums[j], nums[k]))
        
        # return  [list(triplet) for triplet in ans] 
        
