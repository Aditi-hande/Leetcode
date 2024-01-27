class Solution:
    def removeDuplicates(self, s: str, k: int) -> str:
        st=[]
        
        for char in s:
            
            
            if st and st[-1][0]==char:
                st[-1][1]+=1
                
            else:
                st.append([char,1])
            
            if st[-1][1]==k:
                st.pop()
        
        
        return "".join(c * freq for c, freq in st)
                
            
        