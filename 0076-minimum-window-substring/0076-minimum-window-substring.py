class Solution:
    def minWindow(self, s: str, t: str) -> str:

        if not s or not t or len(s)<len(t):
            return ""

        scnt=Counter()
        tcnt=Counter(t)
        count= len(tcnt.keys())
        match=0
        i,j=0,-1
        ans=""

        while i<len(s):

            if match<count:
                if j==len(s)-1:
                    return ans
                j+=1
                scnt[s[j]]+=1

                if tcnt[s[j]]>0 and scnt[s[j]]==tcnt[s[j]]:
                    match+=1
            else:

                
                scnt[s[i]]-=1

                if tcnt[s[i]]>0 and scnt[s[i]]<tcnt[s[i]]:
                    match-=1
                i+=1

            if match==count:
                if not ans:
                    ans=s[i:j+1]
                elif j-i+1 < len(ans):
                    ans=s[i:j+1]

        return ans

        




        