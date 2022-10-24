class Solution:
    def breakPalindrome(self, palindrome: str) -> str:
        
        n = len(palindrome)
        
        if n <= 1:
            return ""
        
        for i in range(n):
            if palindrome[i] != 'a':
                if n % 2 != 0 and n // 2 == i:
                    continue
                return palindrome[:i] + 'a' + palindrome[i+1:]
        
        return palindrome[:n-1] + 'b'
    
                    