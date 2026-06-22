class Solution:

    def sortStrings(self, input: str) -> str:
        input_arr = list(input)
        for i in range(1, len(input_arr)):
            curr_element = input_arr[i]
            j = i-1
            while(j>=0 and input_arr[j] > curr_element):
                input_arr[j+1] = input_arr[j]
                j = j - 1
            input_arr[j+1] = curr_element
        return ''.join(input_arr)

    # by sorting
    def isAnagram(self, s: str, t: str) -> bool:
        return sorted(s) == sorted(t)

        