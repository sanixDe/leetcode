class Solution:
    def breakPalindrome(self, palindrome: str) -> str:
        
        if len(palindrome) == 1:
            return ""
        
        if len(palindrome) % 2 == 0:
            
            for i in range(len(palindrome)):
                if ord(palindrome[i]) > 97:
                    palindrome = palindrome[:i] + "a" + palindrome[i+1:]
                    return palindrome
                elif i == len(palindrome) -1:
                    palindrome = palindrome[:i] + chr(ord(palindrome[i])+1) + palindrome[i+1:]
                    return palindrome
        else:

            for i in range(len(palindrome)):
                if i != len(palindrome) // 2:

                    if ord(palindrome[i]) > 97:
                        palindrome = palindrome[:i] + "a" + palindrome[i+1:]
                        return palindrome
                    elif i == len(palindrome) -1:
                        palindrome = palindrome[:i] + chr(ord(palindrome[i])+1) + palindrome[i+1:]
                        return palindrome

                    