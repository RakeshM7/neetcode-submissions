class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        tracker = {}
        for i in range(0, len(nums)):
            if (target-nums[i]) in tracker.keys():
                return [tracker.get(target-nums[i]), i]
            else:
                tracker[nums[i]] = i