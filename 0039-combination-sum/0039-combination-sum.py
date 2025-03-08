class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        # res=[]
        # def backtrack(start,target,path):
        #     if target==0:
        #         res.append(list(path))
        #         return
        #     for i in range(start,len(candidates)):
        #         if candidates[i]>target:
        #             continue
        #         path.append(candidates[i])
        #         backtrack(i,target-candidates[i],path)
        #         path.pop()
        

        # backtrack(0,target,[])
        # return res
        res=[]
        def backtrack(i,cur,total):
            if total==target:
                res.append(cur.copy())
                return
            if i>=len(candidates) or total>target:
                return
            cur.append(candidates[i]) 
            backtrack(i,cur,total+candidates[i])
            cur.pop()
            backtrack(i+1,cur, total)
        backtrack(0,[],0)
        return res
