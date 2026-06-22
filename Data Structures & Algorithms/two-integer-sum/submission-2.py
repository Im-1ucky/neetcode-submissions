class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        targets = {}
        for i, num in enumerate(nums):
            complement = target - num
            if complement in targets:
                return [targets[complement], i]
            targets[num] = i
