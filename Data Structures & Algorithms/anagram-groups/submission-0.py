class Solution:

    def isAnagram(self, str1: str, str2: str) -> bool:
        return sorted(str1) == sorted(str2)

    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        result_arr = []
        for i in range(0, len(strs)):
            if len(result_arr) == 0:
                result_arr.append([strs[i]])
            else:
                flag = 0
                for j in range(0, len(result_arr)):
                    if self.isAnagram(result_arr[j][0], strs[i]):
                        result_arr[j].append(strs[i])
                        flag = 1
                if flag == 0:
                    result_arr.append([strs[i]])
                    
        return result_arr

        