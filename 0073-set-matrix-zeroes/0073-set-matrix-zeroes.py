class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        row=len(matrix)
        col=len(matrix[0])
        r=[0]*row
        c=[0]*col
        for i in range(row):
            for j in range(col):
                if matrix[i][j]==0:
                    r[i]=1
                    c[j]=1
        for i in range(row):
            for j in range(col):
                if r[i]==1 or c[j]==1:
                    matrix[i][j]=0
        return matrix