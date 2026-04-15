class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        
        if not intervals:
            return 0

        intervals.sort(key=lambda x: x[1])

        S = []
        S.append(intervals[0])

        for i in range(1, len(intervals)):
            current_ends = intervals[i][0]

            last_finish = S[-1][1]

            if current_ends >= last_finish:
                S.append(intervals[i])

        return len(intervals) - len(S)
