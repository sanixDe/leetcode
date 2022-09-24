class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        dict = {}

        for i in nums:
            if i in dict:
                dict[i] += 1
            else:
                dict[i] = 1
        res = []
        for w in sorted(dict, key=dict.get, reverse=True):
            if k > 0:
                res.append(w)

            else:
                break
            k -= 1
        return(res)