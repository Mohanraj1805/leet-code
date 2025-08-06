class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        def left():
            l=0
            r=len(nums)-1
            ans=-1
            while l<=r:
                mid=(l+r)//2
                if nums[mid]< target:
                    l=mid+1
                else:
                    if nums[mid]==target:
                        ans=mid
                    r=mid-1
            return ans
        def right():
            l=0
            r=len(nums)-1
            ans=-1
            while l<=r:
                mid=(l+r)//2
                if nums[mid] >target:
                    r=mid-1
                else:
                    if nums[mid]==target:
                        ans=mid
                    l=mid+1
            return ans
        if not nums:
            return [-1,-1]
        left_index=left()
        if left_index==-1:
            return [-1,-1]
        right_index=right()
        return [left_index,right_index]
        