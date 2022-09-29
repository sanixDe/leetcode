class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:


        pre = [nums[0]]
        post = [0] * len(nums)
        post[-1] = nums[-1]
        ans = []
        for i in range(1, len(nums)):
            pre.append(pre[i-1] * nums[i])


        for i in range(len(nums)-2, -1, -1):
            # print(i, nums[i])
            post[i] = post[i+1]*nums[i]

        for i in range(len(nums)):
            if i==0:
                ans.append(post[i+1])
            elif i == len(nums)-1:
                ans.append(pre[i-1])
            else:
                ans.append(pre[i-1]*post[i+1])


        return(ans)