class Solution:
    def maxArea(self, heights: List[int]) -> int:
        max_area = 0
        ranges = []
        for i in range(0, len(heights) - 1):
            for j in range(i+1, len(heights)):
                curr_area = (j-i) * min(heights[i], heights[j])
                if curr_area > max_area:
                    max_area = curr_area
                    ranges.append([i,j])
        print(ranges)
        return max_area

        