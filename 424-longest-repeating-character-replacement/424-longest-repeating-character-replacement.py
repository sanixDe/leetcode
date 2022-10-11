class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        freq = {}
        l = 0
        res = 0
        
        for r in range(len(s)):
            
            if s[r] in freq:
                freq[s[r]] += 1
            else:
                freq[s[r]] = 1
            
            while r-l+1 - max(freq.values()) > k:
                freq[s[l]] -= 1
                l += 1
                
            res = max(res, r-l+1)
            
        return res