class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        map=defaultdict(list)
        
        def getdist(i,j):
            return pow((pow((i),2)+ pow((j),2)),0.5)
        
        for pt in points:
            map[getdist(pt[0],pt[1])].append([pt[0],pt[1]])
        
        key=sorted(map)
        
        ans=[]
        i=k
        j=0
        while i!=0:
            ans.extend(x for x in map[key[j]])
            i=i-len(map[key[j]])
            j+=1
        return ans
            
            
        