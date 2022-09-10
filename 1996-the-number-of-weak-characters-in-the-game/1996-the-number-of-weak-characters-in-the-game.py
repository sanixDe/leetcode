class Solution:
    def numberOfWeakCharacters(self, properties: List[List[int]]) -> int:
        properties.sort()

        res = 0
        max_a, max_b = cur_a, cur_b = properties.pop()
        while properties:
            _a, _b = properties.pop()
            if cur_a != _a: 
                max_b, cur_b = max(max_b, cur_b), _b  
                cur_a = _a  

            if max_b > _b and max_a > _a: res += 1

        return res