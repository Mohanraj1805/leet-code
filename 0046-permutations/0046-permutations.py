# class Solution:
#     def permute(self, nums: List[int]) -> List[List[int]]:
#         res=[]
#         #base case
#         if len(nums)==1:
#             return [nums.copy()]
#         for i in range(len(nums)):
#             n=nums.pop(0)
#             perms=self.permute(nums)
#             for perm in perms:
#                 perm.append(n)
#             res.extend(perms)
#             nums.append(n)
#         return res

class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        result = []
        self.backtrack(result, [], nums)
        return result

    def backtrack(self, result: List[List[int]], temp: List[int], nums: List[int]):
        # If temp contains all numbers, add a copy to the result
        if len(temp) == len(nums):
            result.append(temp[:])  # Append a copy of temp
            return
        
        for num in nums:
            # Skip if the number is already used
            if num in temp:
                continue
            
            # Choose the number
            temp.append(num)
            
            # Explore further
            self.backtrack(result, temp, nums)
            
            # Undo the choice (backtrack)
            temp.pop()
