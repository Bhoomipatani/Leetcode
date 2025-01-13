class Solution:
    def reorderLogFiles(self, logs: List[str]) -> List[str]:
        mapp={}
        i=0
        while i<len(logs):
            checklog=list(logs[i].split(' '))
            letterlog=False
            for j in range(1,len(checklog)):
                if (checklog[j]).isdigit():
                    letterlog=False
                    break
                else:
                    letterlog=True
            if letterlog==True:
                mapp[logs[i]]=' '.join(checklog[1:])
                logs.pop(i)
            else:    
                i+=1
        mapp=sorted(mapp.items(), key=lambda x:x[0], reverse=True)
        mapp=sorted(mapp, key=lambda x:x[1], reverse=True)
        for k,v in mapp:
            insertlog=k
            logs.insert(0,insertlog)
        return logs