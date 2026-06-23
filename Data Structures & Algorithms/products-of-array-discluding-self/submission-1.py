class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        result_arr = []
        total_prod = 1
        non_zero_prod = 1
        zero_count = 0
        for i in range(0, len(nums)):
            total_prod *= nums[i]
            if nums[i] != 0:
                non_zero_prod *= nums[i]
            else:
                zero_count += 1
        for itr in nums:
            if itr != 0:
                result_arr.append(math.floor(total_prod/itr))
            elif itr == 0:
                if zero_count > 1:
                    result_arr.append(0)
                else:
                    result_arr.append(non_zero_prod)
        return result_arr