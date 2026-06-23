class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        sortedTracker = {}
        for value in strs:
            key = "".join(sorted(value))
            if key in sortedTracker:
                sortedTracker[key].append(value)
            else:
                sortedTracker[key] = [value]
        return list(sortedTracker.values())