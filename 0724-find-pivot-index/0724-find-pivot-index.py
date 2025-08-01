class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        total=0
        for i in nums:
            total+=i
        left=0
        for i in range(len(nums)):
            right=total-left-nums[i]
            if right==left:
                return i
            left+=nums[i]
        return -1
