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
    
    # Using Sort
    def hasDuplicate(self, nums: List[int]) -> bool:
        self.insertionSort(nums)
        for i in range(0,len(nums)-1):
            if nums[i] == nums[i+1]:
                return True
        return False