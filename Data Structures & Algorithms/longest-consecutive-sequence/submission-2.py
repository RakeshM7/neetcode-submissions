class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        sortedArray = list(dict.fromkeys(sorted(nums)))
        if len(sortedArray) == 0:
            return 0
        elif len(sortedArray) == 1:
            return 1
        print(sortedArray)
        maximumLongestSubsequence = 0
        result = []
        ptr = 0
        while ptr < len(sortedArray) - 1:
            ssBegin = ptr
            curr_result = []
            while (ptr < len(sortedArray) - 1) and abs(sortedArray[ptr] - sortedArray[ptr+1]) == 1:
                curr_result.append(sortedArray[ptr])
                ptr = ptr + 1
            curr_result.append(sortedArray[ptr])
            ssLength = ptr - ssBegin + 1
            if ssLength > maximumLongestSubsequence:
                maximumLongestSubsequence = ssLength
                result = curr_result
            ptr = ptr + 1
        return maximumLongestSubsequence





        