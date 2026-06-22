class Solution:
    def insertionSort(self, arr) -> List[int]:
        for i in range(1,len(arr)):
            curr_element = arr[i]
            j = i-1
            while(j >= 0 and arr[j] > curr_element):
                arr[j+1] = arr[j]
                j = j-1
            arr[j+1] = curr_element
        return arr
        
    def hasDuplicateWithSort(self, nums: List[int]) -> bool:
        self.insertionSort(nums)
        for i in range(0,len(nums)-1):
            if nums[i] == nums[i+1]:
                return True
        return False
    
    def hasDuplicateWithHash(self, nums: List[int]) -> bool:
        result_hash = {}
        for num in nums:
            if result_hash.get(num):
                return True
            else:
                result_hash[num] = 1
        return False
    
    def hasDuplicate(self, nums: List[int]) -> bool:
        result_set = set(nums)
        return len(result_set) != len(nums)