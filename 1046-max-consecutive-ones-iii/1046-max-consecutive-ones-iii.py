class Solution:
    def longestOnes(self, nums: list[int], k: int) -> int:
        l = 0
        max_one = 0
        zero = 0
        
        for r in range(len(nums)): 
            if nums[r] == 0:
                zero += 1
            while zero > k:
                if nums[l] == 0:
                    zero -= 1
                l += 1
            max_one = max(max_one, r - l + 1)  
        return max_one
