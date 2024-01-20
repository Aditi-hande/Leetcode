class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        intervals.sort(key=lambda x:x[1])
        
        prev,cnt=0,1 #already taking interval[0]
        
        for i in range(1,len(intervals)):
            if intervals[prev][1]<=intervals[i][0]:
                cnt+=1
                prev=i

        return len(intervals)-cnt

        #insted of removing overlap think as attending max meetings.
        