from itertools import combinations
class Solution:
    def mostVisitedPattern(self, username: List[str], timestamp: List[int], website: List[str]) -> List[str]:
        mapp={}
        count={}
        sorted_data = sorted(zip(username, timestamp, website), key=lambda x: x[1])
        username, timestamp, website = zip(*sorted_data)
        for i in range(len(timestamp)):
            if username[i] not in mapp:
                mapp[username[i]]=website[i]
            else:
                mapp[username[i]]+=','
                mapp[username[i]]+=website[i]
        mapp=dict(sorted(mapp.items(), key=lambda x:x[1]))
        # print(mapp)
        for value in mapp.values():
            valuearr=value.split(',')
            if len(valuearr)>=3:
                valuearr = list(set(combinations(valuearr, 3)))
                # print(valuearr)
                for val in valuearr:
                    if val not in count:
                        count[val]=1
                    else:
                        count[val]+=1
           
        count=dict(sorted(count.items(), key=lambda x:x[0]))      
        # print(count)
        keymax = max(count, key=count.get)
        return list(keymax)
            
            