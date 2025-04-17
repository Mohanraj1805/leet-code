class Solution:
    def maxScore(self, cardPoints: List[int], k: int) -> int:
        lsum=0
        rsum=0
        maxsum=0
        for i in range(k):
            lsum+=cardPoints[i]
        maxsum=lsum
        for i in range(1,k+1):
            lsum-=cardPoints[k-i]
            rsum+=cardPoints[-i]
            maxsum=max(maxsum,lsum+rsum)
        return maxsum
