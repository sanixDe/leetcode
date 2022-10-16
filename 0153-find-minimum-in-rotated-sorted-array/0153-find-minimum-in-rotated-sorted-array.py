class Solution:
    def findMin(self, nums: List[int]) -> int:
        l = 0
        r = len(nums)-1
        min_res = nums[0]
        
        while l <= r:
            if nums[l] < nums[r]:
                min_res = min(min_res, nums[l])
                break
        
            mid = (l+r) // 2
            min_res = min(min_res, nums[mid])
            if nums[mid] >= nums[l]:
                
                l = mid+1
            else:
                r = mid-1
        return min_res