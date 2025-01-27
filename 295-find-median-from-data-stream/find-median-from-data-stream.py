class MedianFinder:

    def __init__(self):
        self.numarr=[]

    def addNum(self, num: int) -> None:
        self.numarr.append(num)
        

    def findMedian(self) -> float:
        n=len(self.numarr)
        self.numarr.sort()
        # print(self.numarr,n)
        if n%2==0:
            return (self.numarr[n//2]+self.numarr[(n-1)//2])/2
        else:
            # print(self.numarr[(n-1)//2])
            return self.numarr[(n-1)//2]


# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()