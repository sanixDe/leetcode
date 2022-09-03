class Solution:
    def numsSameConsecDiff(self, n: int, k: int) -> List[int]:
        res = []
        if n == 1:
            res.append(0)

        def dfs(num, n):
            if n == 0:
                res.append(num)
                return
            x = num%10
            if x-k > -1:
                dfs(num*10+(x-k), n-1)
            if k > 0 and x+k < 10:
                dfs(num*10+(x+k), n-1)


        for i in range(1,10):
            dfs(i, n-1)
        return(res)