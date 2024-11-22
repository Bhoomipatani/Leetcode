class Solution:
    def reverseVowels(self, s: str) -> str:
        s_list = list(s)
        vowels = {'a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U'}
        arr = [char for char in s_list if char in vowels]
        
        n = len(arr)
        k = 1
        
        for i in range(len(s_list)):
            if s_list[i] in vowels:
                s_list[i] = arr[n-k]
                k += 1
        
        return ''.join(s_list)

