class Solution:
    def romanToInt(self, s: str) -> int:
        dict={"I":1,"V":5,"X":10,"L":50,"C":100,"D":500,"M":1000}

        if not s:
            return 0

        ans=i=0
        while i<len(s):
            if i!=len(s)-1 and dict[s[i+1]]>dict[s[i]]:
                ans+=dict[s[i+1]]-dict[s[i]]
                i+=2
                # print(i,ans)
            else:
                ans+=dict[s[i]]
                i+=1
                # print(i,ans)
        return ans


        