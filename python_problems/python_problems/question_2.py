class Solution:
    def countOdds(self,low: int,high: int)-> int:
        return (high+1)//2 -(low//2)

obj=Solution()
print(obj.countOdds(3,7))    