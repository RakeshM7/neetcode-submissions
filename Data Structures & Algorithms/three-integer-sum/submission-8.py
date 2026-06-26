class Solution:
    def threeSumBrute(self, nums: List[int]) -> List[List[int]]:
        result = []
        nums_set = set()
        for i in range(0, len(nums) - 2):
            for j in range(i + 1, len(nums) - 1):
                if i == j:
                    continue
                for k in range(j + 1, len(nums)):
                    if j == k or i == k:
                        continue
                    if nums[i] + nums[j] + nums[k] == 0:
                        item = sorted([nums[i], nums[j], nums[k]])
                        if item not in result:
                            result.append(item)
        return result

    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        print(nums)
        result = []
        target = 0
        for i in range(0, len(nums) - 2):
            left_ptr = i + 1
            right_ptr = len(nums) - 1
            print(f"i value: {nums[i]} | Left: {nums[left_ptr]} | Right: {nums[right_ptr]} | Target: {target}")
            while(left_ptr < right_ptr):
                curr_sum = nums[i] + nums[left_ptr] + nums[right_ptr]
                if curr_sum < target:
                    left_ptr += 1
                elif curr_sum > target:
                    right_ptr -= 1
                elif curr_sum == target:
                    if [nums[i], nums[left_ptr], nums[right_ptr]] not in result:
                        result.append([nums[i], nums[left_ptr], nums[right_ptr]])
                    left_ptr += 1
                    right_ptr -= 1
        return result
        
            
