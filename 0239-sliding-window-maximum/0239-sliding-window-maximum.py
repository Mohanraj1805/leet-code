class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        # st=[]
        # if len
        # for i in range(len(nums)-k+1):
        #     max_num=nums[0]
        #     for j in range(i,i+k):
        #         max_num=max(max_num,nums[j])
        #     st.append(max_num)
        # return st
        output=[]
        q=collections.deque()
        l=r=0
        while r<len(nums):
            #pop the smaller values from deque
            while q and nums[q[-1]] < nums[r]:
                q.pop()
            q.append(r)
            # remove left val from window
            if q[0]<l:
                q.popleft()
            if (r-l+1)>=k:
                output.append(nums[q[0]])
                l+=1
            r+=1
        return output