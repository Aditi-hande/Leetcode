class Solution {
public:
    bool backspaceCompare(string s, string t) {
        stack<char> st;
        for(char i:s){
            if(i=='#' && !st.empty())st.pop();
            if(i!='#'){st.push(i);}
        }
        string temp,temp1;
        while(!st.empty()){
            temp=temp+st.top();
            st.pop();
        }
        
        
        
        for(auto i:t){
            if(i=='#'&& !st.empty())st.pop();
            if(i!='#'){st.push(i);}
        }
        while(!st.empty()){
            temp1=temp1+st.top();
            st.pop();
        }
        //cout<<temp<<"  "<<temp1;
        return(temp==temp1);
        
    }
};