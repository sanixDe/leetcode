class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        dict = {}
        for i in strs:
            alpha = [0] * 26
            for j in i:
                val = ord(j)-97
                alpha[val] += 1

            if tuple(alpha) in dict:
                dict[tuple(alpha)].append(i)
            else:
                dict[tuple(alpha)] = [i]


        return(list(dict.values()))
    
        # time complexity O(mn) m = len(strs) and  n = len(str[i])