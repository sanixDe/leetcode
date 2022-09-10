class Solution:
    def numberOfWeakCharacters(self, properties: List[List[int]]) -> int:
        properties.sort()

        res = 0
        max_a, max_b = cur_a, cur_b = properties.pop()
        while properties:
            _a, _b = properties.pop()
            if cur_a != _a:  # 当a切换
                max_b, cur_b = max(max_b, cur_b), _b  # 更新全局最大b，并缓存当前a对应的局部最大b
                cur_a = _a  # 缓存当前a

            if max_b > _b and max_a > _a: res += 1

        return res