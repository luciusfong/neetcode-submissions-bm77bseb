class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        found=dict()
        for i in range(0,len(nums)):
            a=nums[i]
            b=target-nums[i]
            if b in found:
                return [found[b], i]
            else:
                found[a]=i