class Solution:
    def chk(self, word:str, word2:str,look)->bool:
        i=j=0
        while i<len(word) and j<len(word2):
            if(look[word[i]]<look[word2[j]]):
                return True
            elif(look[word[i]]>look[word2[j]]):
                print(word[i],word2[j])
                return False
            i+=1
            j+=1
        return len(word)<=len(word2)

    def isAlienSorted(self, words: List[str], order: str) -> bool:
        look={order[i]:i for i in range(len(order))}

        for i in range(len(words)-1):
            w=words[i]
            w1=words[i+1]


            ans=self.chk(w,w1,look)
            if not ans:
                return False
        return True


        