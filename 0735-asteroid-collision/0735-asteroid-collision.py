class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        st=[]
        for i in asteroids:
            if i >0: # i is positive
                st.append(i)
            else:
                while st and st[-1]>0 and st[-1]<abs(i): # time of collision 
                    st.pop()
                if st and st[-1]==abs(i): # in collision when both has same value
                    st.pop()
                elif len(st)==0 or st[-1] < 0: # if any remaining elements
                    st.append(i)
        return st