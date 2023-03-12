class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:

        res = []
        nums.sort()
        for i in range(len(nums)):
            
            if nums[i] > 0:
                return res
            if i > 0 and nums[i]== nums[i-1]:
                continue
            l = i+1
            r = len(nums)-1

            while l < r:
                # print(nums[l] + nums[r] + nums[i], i, l ,r)
                if nums[l] + nums[r] + nums[i] == 0:
                    res.append([nums[i],nums[l], nums[r]])
                    l +=1
                    while nums[l] == nums[l-1] and l<r:
                        l += 1
                elif nums[l]+nums[r]+nums[i] > 0:
                    r -= 1
                else:
                    l += 1
        return res