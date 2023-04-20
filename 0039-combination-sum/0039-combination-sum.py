class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        
        def dfs(index, res, path):
            if res == target:
                # print("path",path)
                ans.append(path)
                return 
            
            if res > target:
                return 
            
            for nxt_idx in range(index, l):
                # print(index, nxt_idx, candidates[nxt_idx], res, path)
                dfs(nxt_idx, res+candidates[nxt_idx], path+[candidates[nxt_idx]])

            
            return ans
        l = len(candidates)
        
        ans = []
        
        for i in range(l):
            dfs(i, candidates[i], [candidates[i]])
#             if val != []:
#                 ans.append(val)
            
        return ans