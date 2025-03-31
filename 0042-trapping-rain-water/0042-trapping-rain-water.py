class Solution:
    def trap(self, height: List[int]) -> int:
        #BRUTE FORCE METHOD
        # count=0
        # if not height:
        #     return 0
        # for i in range(len(height)):
            
            
        #     leftmax = max(height[:i+1])  # Max height on the left
        #     rightmax = max(height[i:])   # Max height on the right
        #     if height[i]<leftmax and height[i]< rightmax:
        #         count +=min(leftmax, rightmax) - int(height[i])
              
        
        # return count


        #OPTIMIZED CODE USING TWO POINTER 
        l=0
        r=len(height)-1
        leftmax=rightmax=count=0
        while l<r:
            if height[l] < height[r]:
                if height[l] >= leftmax:
                    leftmax = height[l]
                else:
                    count+= leftmax - height[l]
                l+= 1
            else:
                if height[r] <= height[l]:
                    if height[r] >= rightmax:
                        rightmax = height[r]
                    else:
                        count+= rightmax - height[r]
                    r-= 1
        return count