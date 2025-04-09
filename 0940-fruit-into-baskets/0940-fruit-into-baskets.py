class Solution:
    def totalFruit(self, fruits: List[int]) -> int:
        l=max_one=0
        basket=collections.defaultdict(int)
        for r in range(len(fruits)):
            basket[fruits[r]]+=1
            
            while len(basket)>2:
                basket[fruits[l]]-=1
                if  basket[fruits[l]]==0:
                    del  basket[fruits[l]]
                l+=1
            max_one=max(max_one,r-l+1)
        return max_one