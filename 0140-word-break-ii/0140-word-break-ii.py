class Solution:
    
    
    
    def wordBreak(self, s: str, wordDict: List[str]) -> List[str]:
        mp=defaultdict(list)
        
        if not s:
            return []
        
        if s in mp:
            return mp[s]
        
        res=[]
        for i in range(len(wordDict)):
            if not s.startswith(wordDict[i]):
                continue
                
            if len(s)==len(wordDict[i]):
                res.append(s)

            else:
                restans= self.wordBreak(s[len(wordDict[i]):],wordDict)
                if restans !=[]:
                    for ans in restans:
                        temp= wordDict[i]+ " " + ans
                        res.append(temp)
                    
        mp[s]=res

        return res
                    
            
        