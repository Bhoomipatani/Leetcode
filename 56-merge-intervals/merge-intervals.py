class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals=sorted(intervals, key= lambda x:x[0])
        i=0
        while i<len(intervals)-1:
            if intervals[i][1]>=intervals[i+1][0] and intervals[i][1]<=intervals[i+1][1]:
                intervals[i][1]=intervals[i+1][1]
                intervals.pop(i+1)
            elif intervals[i][1]>=intervals[i+1][0] and intervals[i][1]>=intervals[i+1][1]:
                intervals.pop(i+1)
            else:
                i+=1
        return intervals