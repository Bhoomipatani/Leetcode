class Solution:
    def compareVersion(self, version1: str, version2: str) -> int:
        a1=version1.split('.')
        a2=version2.split('.')

        if len(a1)>len(a2):
            for i in range(len(a1)-len(a2)):
                a2.append('0')
        if len(a1)<len(a2):
            for i in range(len(a2)-len(a1)):
                a1.append('0')
        i,j=0,0
        while i<len(a1) and j<len(a2):
            if int(a1[i])>int(a2[j]):
                return 1
            elif int(a1[i])<int(a2[j]):
                return -1  
            i+=1
            j+=1
        return 0
