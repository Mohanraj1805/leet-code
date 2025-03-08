class Solution(object):
    def generate(self, numRows):
        """
        :type numRows: int
        :rtype: List[List[int]]
        """
        def generated_row(row_index):
            ans=1
            ansrow=[1]
            for i in range(1,row_index):

                ans=ans*(row_index-i)
                ans//=i
                ansrow.append(ans)
            return ansrow
        result=[]
        for i in range(1,numRows+1):
            result.append(generated_row(i))
        return result