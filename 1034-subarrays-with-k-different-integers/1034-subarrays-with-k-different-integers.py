class Solution:
    def subarraysWithKDistinct(self, nums: List[int], k: int) -> int:
        def atmost(k):
            l = 0
            set_k = {}
            cnt = 0
            for r in range(len(nums)):
                set_k[nums[r]] = set_k.get(nums[r], 0) + 1
                
                while len(set_k) > k:
                    set_k[nums[l]] -= 1
                    if set_k[nums[l]] == 0:
                        del set_k[nums[l]]
                    l += 1

                cnt += r - l + 1
            return cnt
        
        return atmost(k) - atmost(k - 1)
        # adding sub arr with less than k => atmost(k)
        # adding sub arr with less than k-1 => atmost(k-1)
        # if sub both the condition we will get sub arr with == k
