class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        
        def left():
            l=0
            r=len(nums)-1
            index=-1
            while l<=r:
                mid=(l+r)//2
                if nums[mid]==target:
                    index=mid
                    r=mid-1

                elif nums[mid]<target:
                    l=mid+1
                elif nums[mid]>target:
                    r=mid-1
            return index
        def right():
            l=0
            r=len(nums)-1
            index=-1
            while l<=r:
                mid=(l+r)//2
                if nums[mid]==target:
                    index=mid
                    l=mid+1
                elif nums[mid]<target:
                    l=mid+1
                elif nums[mid]>target:
                    r=mid-1
            return index
        return [left(),right()]


     