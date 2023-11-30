class Solution:
    def hammingWeight(self, n: int) -> int:
        ans=0
        temp=bin(n)[2:]
        for s in temp:
            if(s=='1'):
                ans+=1
        return ans
        