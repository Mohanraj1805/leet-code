class Solution(object):
    def fourSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        # n=len(nums)
        # st=set()
        # for i in range(n):
        #     for j in range(i+1,n):
        #         hashset = set()
        #         for k in range(j+1,n):
        #             sum_=nums[i] + nums[j] + nums[k]
        #             fourth = target - sum_
        #             if fourth in hashset:
        #                 temp = [nums[i], nums[j], nums[k], fourth]
        #                 temp.sort()
        #                 st.add(tuple(temp))
        #         # put the kth element into the hashset:
        #             hashset.add(nums[k])
        # ans = [list(t) for t in st]
        # return ans
        # n=len(nums)
        # nums.sort()
        # ans=[]
        # for i in range(n):
        #     if i>0 and nums[i]==nums[i-1]:
        #         continue
        #     for j in range(i+1,n):
        #         if j>i+1 and nums[j]==nums[j-1]:
        #             continue
        #         k=j+1
        #         last=n-1
        #         while k<last:
        #             _sum = nums[i] + nums[j] + nums[k] + nums[last]
        #             if _sum==target:
        #                 temp=  nums[i] , nums[j] , nums[k] , nums[last]
        #                 ans.append(temp)
        #                 k+=1
        #                 last-=1
        #                 while k<last and nums[k]==nums[k-1]:
        #                     k+=1
        #                 while k<last and nums[last]==nums[last+1]:
        #                     last-=1
        #             elif _sum<target:
        #                 k+=1
        #             elif _sum>target:
        #                 last-=1
        # return ans 

        nums.sort()
        res=set()
        for i in range(len(nums)):
            if i>0 and nums[i]==nums[i-1]:
                continue
            for j in range(i+1,len(nums)):
                if j>i+1 and nums[j]==nums[j-1]:
                    continue
                k,l=j+1,len(nums)-1
                tar=target-(nums[i]+nums[j])
                while k<l:
                    if tar==(nums[k]+nums[l]):
                        res.add((nums[i],nums[j],nums[k],nums[l]))
                        k+=1
                        l-=1
                    elif (nums[k]+nums[l]) >tar:
                        l-=1
                    else:
                        k+=1
        return [list(lis) for lis in res]