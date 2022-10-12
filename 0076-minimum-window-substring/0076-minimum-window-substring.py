class Solution:
    def minWindow(self, s: str, t: str) -> str:
        
        if t == "": return ""
        dict_t = {}
        for c in t:
            dict_t[c] = 1 + dict_t.get(c, 0)
            
        dict_s = {}
        l = 0
        have = 0
        need = len(dict_t)
        res, resLen = [-1,-1], float('inf')
        for r in range(len(s)):
            
            c = s[r]
            
            dict_s[c] = 1+ dict_s.get(c, 0)
            
            if c in dict_t and dict_s[c] == dict_t[c]:
                
                have += 1
            
            while have == need:
                if (r-l+1) < resLen:
                    
                    res = [l, r]
                    
                    resLen = (r-l+1)
                    
                dict_s[s[l]] -= 1
                if s[l] in dict_t and dict_s[s[l]] < dict_t[s[l]]:
                    have -= 1
                l += 1
        l,r = res
        return s[l : r + 1] if resLen != float("infinity") else ""
    
    
    '''
    Time Complexity = O(N)
    space Complexity = O(1)
    
    '''
        


















