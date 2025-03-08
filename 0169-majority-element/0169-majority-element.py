#__import__("atexit").register(lambda: open("display_runtime.txt", "w").write("0"))
class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # nums.sort()
        # l=0
        # r=len(nums)-1
        # return nums[(l+r)//2]
        # majority=nums[0]
        # vote=0
        # for i in range(len(nums)):
        #     if nums[i]==majority:
        #         vote+=1
        #     else:
        #         if vote<=0:
        #             majority=nums[i]
        #             vote+=1
        #         else:
        #             vote-=1
        # return majority
        majority=nums[0]
        votes=0
        for i in range(len(nums)):
            if votes==0:
                majority=nums[i]
                votes+=1
            elif majority==nums[i]:
                votes+=1
            else:
                votes-=1
        return majority