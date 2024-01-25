class Solution:
    def minAddToMakeValid(self, s: str) -> int:
        st=[]
        ans=0
        
        for i in range (len(s)):
            if s[i]=="(":
                st.append(i)
            else:
                if st:
                    st.pop()
                else:
                    ans+=1
        while(st):
            st.pop()
            ans+=1
        
        return ans 
        