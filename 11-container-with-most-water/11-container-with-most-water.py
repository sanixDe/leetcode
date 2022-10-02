class Solution:
    def maxArea(self, height: List[int]) -> int:
        max_area = 0
        left, right = 0, len(height) - 1
        
        while left < right:
            
            temp_area = (right-left) * min(height[left], height[right])
            max_area = max(temp_area, max_area)
            
            if height[left] < height[right]:
                left += 1
            elif height[left] > height[right]:
                right -= 1
            else:
                if left+1<right and right - 1> left and height[left+1] < height[right-1]:
                    left+= 1
                else:
                    right -= 1
        
        return max_area
    
        
        # time complexity = O(n)
        # space complecity = O(1)