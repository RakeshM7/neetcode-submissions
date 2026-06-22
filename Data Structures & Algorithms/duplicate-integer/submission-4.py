class Solution:
    # Using Hash Map
    def hasDuplicate(self, nums: List[int]) -> bool:
        result_hash = {}
        for num in nums:
            if result_hash.get(num):
                return True
            else:
                result_hash[num] = 1
        return False