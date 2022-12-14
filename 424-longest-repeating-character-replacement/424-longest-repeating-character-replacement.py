class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        freq = {}
        l = 0
        res = 0
        
        for r in range(len(s)):
            freq[s[r]] = 1 + freq.get(s[r], 0)

            while r-l+1 - max(freq.values()) > k:
                freq[s[l]] -= 1
                l += 1
                
            res = max(res, r-l+1)
            
        return res
    
        '''
                Time Complexity = O(26 * N) 26 for the freq hashmap
                Space Complexity = O(1) Because we are using constant hashmap
        '''