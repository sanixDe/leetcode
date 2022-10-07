class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        max_len = 0
        if len(s) < 2:
            return len(s)
        sett = set()
        start = 0
        for i in range(len(s)):
            
            while s[i] in sett:
                sett.remove(s[start])
                start += 1
            # else:
            sett.add(s[i])
            max_len = max(max_len, i-start+1)
        
        return max_len
                
        
    
    '''
    a b c a b c b b
    s e
    
    dict = {}
    
    
    
    
    
    
    
    
    
    
    '''