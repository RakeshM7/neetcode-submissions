class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        tracker = {}
        for num in nums:
            if num in tracker:
                tracker[num] += 1
            else:
                tracker[num] = 1
        flattened_tracker = tracker.items()
        sorted_flattened_tracker = sorted(flattened_tracker, key=lambda x: x[1], reverse=True)
        result_arr = [t[0] for t in sorted_flattened_tracker[:k]]
        return result_arr

        
         


        