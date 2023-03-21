class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        l = 0
        
        n = len(s)
        
        str_set = set()
        max_len = 0
        for r in range(n):
            while s[r] in str_set:
                str_set.remove(s[l])
                l += 1
            str_set.add(s[r])
            print(str_set,l, r,len(s[l:r+1]))
            max_len = max(max_len, len(s[l:r+1]) )
            # print(max_len)
        return max_len
    
    # time complexity O(N)