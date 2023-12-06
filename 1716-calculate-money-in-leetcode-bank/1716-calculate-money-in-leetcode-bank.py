class Solution:
    def totalMoney(self, n: int) -> int:
        q, r = divmod(n, 7)
        return int((28+7*(q-1)/2)*q + ((r+1)/2+q)*r)        