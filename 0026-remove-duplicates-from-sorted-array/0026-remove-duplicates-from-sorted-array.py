class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # ans=set()
        # res=[]
        # count=0
        # length=len(nums)
        # for i in nums:
        #     if i not in ans:
        #         ans.add(i)
        #         res.append(i)
        #         count+=1
        # newlength=len(res)
        # final_len=length-newlength
        # remaining_num=['_']*final_len
        # return count,res+remainig_num

                
        n=len(nums)
        j=1
        for i in range(1,n):
            if nums[i]!=nums[i-1]:
                nums[j]=nums[i]
                j+=1
        return j