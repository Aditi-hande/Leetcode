class Solution:
    def kthGrammar(self, n: int, k: int) -> int:
        if n==1:
            return 0
        if k==1:
            return 0
        
        lenbit= 2** (n-1)
        halflen = lenbit//2
        
        if k>halflen:
            return 1 ^ self.kthGrammar(n-1,k-halflen)
        return self.kthGrammar(n-1,k)
        

        