class Solution:
    def maximumUnits(self, boxType: List[List[int]], trucksize: int) -> int:
        boxType=sorted(boxType, key=lambda x:x[1],reverse=True)
        totalunit=0
        for i in range(len(boxType)):
            if trucksize==0:
                break
            elif trucksize>boxType[i][0]:
                totalunit+=boxType[i][0]*boxType[i][1]
                trucksize-=boxType[i][0]
            elif trucksize<=boxType[i][0] :
                totalunit+=trucksize*boxType[i][1]
                trucksize=0
        return totalunit