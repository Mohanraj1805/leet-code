class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        st=[]
        next_great={}
        for i in reversed(nums2):
            while st and st[-1] <= i:
                st.pop()
            next_great[i]=st[-1] if st else -1
            st.append(i)
        return [next_great[i] for i in nums1]