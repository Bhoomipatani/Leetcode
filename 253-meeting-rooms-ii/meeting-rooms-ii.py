class Solution:
    def minMeetingRooms(self, intervals):
        intervals.sort()
        rooms = []
        for interval in intervals:
            s, e = interval
            heappush(rooms, e)
            if rooms[0] <= s:
                heappop(rooms)
       
        return len(rooms)