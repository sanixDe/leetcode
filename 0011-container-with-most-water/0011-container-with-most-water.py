class Solution:
    def maxArea(self, height: List[int]) -> int:
        
        l = 0
        r = len(height)-1
        
        max_water = 0
        
        while l < r:
            
            temp = min(height[l], height[r])*(r-l)
            if temp > max_water:
                max_water = temp
            
            if height[l] > height[r]:
                r -= 1
            else:
                l += 1
        return max_water
        
        # time complexity = O(N)