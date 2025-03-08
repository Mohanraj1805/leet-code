class Solution(object):
    def searchMatrix(self, matrix, target):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """
        
        # for i in range(len(matrix)):
        #     for j in range(len(matrix[0])):
        #         if matrix[i][j]==target:
        #             return True
                
        # return False
        row=len(matrix)
        col=len(matrix[0])
        l=0
        r=row*col-1
        while l<=r:
            mid=(l+r)//2
            i=mid//col
            j=mid%col
            if matrix[i][j]==target:
                return True
            elif matrix[i][j]<target:
                l=mid+1
            else:
                r=mid-1
        return False
