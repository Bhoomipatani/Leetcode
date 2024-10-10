class Solution:
    def isValid(self, s: str) -> bool:
        arr=[]
        for i in range(len(s)):
            if s[i] in ['(','[','{']:
                arr.append(s[i])
            elif s[i] in [')',']','}'] and len(arr)==0:
                return False
            elif s[i] in [')',']','}']:
                x=arr.pop()
                if x=='(' and s[i]!=')':
                    return False
                if x=='[' and s[i]!=']':
                    return False
                if x=='{' and s[i]!='}':
                    return False
            
        if len(arr)==0:
            return True
        else:
            return False