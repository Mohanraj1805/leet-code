#  class Solution(object):
#      def longestConsecutive(self, nums):
#         """
#         :type nums: List[int]
#         :rtype: int
#         """
#         # if len(nums)==0:
#         #     return 0
#         # num_set=set(nums)
#         # max_len=0
#         # for num in nums:
#         #     if num-1 not in num_set:
#         #         cur_len=1
#         #         nxt_sum=num+1
#         #         while nxt_sum in nums:
#         #             cur_len+=1
#         #             nxt_sum+=1
#         #         max_len=max(max_len,cur_len)
#         # return max_len

#         # num_set = set(nums)
#         # length = 0
#         # for start in nums:
#         #     if start - 1 not in num_set:
#         #         end =  1
#         #         while start+end in num_set:
#         #             end += 1
#         #         length = max(length, end)
#         # return length
class Solution(object):
    def longestConsecutive(self, nums):
	nums.sort()
	longest, cur_longest = 0, min(1, len(nums))
	for i in range(1,len(nums)):
		if nums[i] == nums[i - 1] : continue
		if nums[i] == nums[i - 1] + 1: cur_longest += 1
		else: longest, cur_longest = max(longest, cur_longest), 1
	return max(longest, cur_longest)
    