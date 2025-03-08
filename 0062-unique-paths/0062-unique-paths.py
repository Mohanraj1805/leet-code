class Solution(object):
    def uniquePaths(self, m, n):
        """
        :type m: int
        :type n: int
        :rtype: int
        """
        grid = [[0] * n for _ in range(m)]

        # Iterate over the grid
        for i in range(m):
            for j in range(n):
                # If we are at the first row or first column,
                # there is only one way to reach that cell
                if i == 0 or j == 0:
                    grid[i][j] = 1
                else:
                    # Memoize the number of ways to reach that cell
                    grid[i][j] = grid[i][j - 1] + grid[i - 1][j]

        # Return the number of ways to reach the last cell
        return grid[m - 1][n - 1]
        # def count_path(i,j):
        #     if i==m-1 and j==n-1:
        #         return 1
        #     if i>=m or j>=n:
        #         return 0
        #     return count_path(i+1,j) + count_path(i,j+1) 
        #     # i+1 means moving down and
        #     # j+1 means moving right 
        # return count_path(0,0)