def merge(self, intervals: List[List[int]]) -> List[List[int]]:
    if len(intervals) == 1:
        return intervals
    # oh boy,t lambda function
    intervals = sorted(intervals, key = lambda x: x[0])
        
    ans = []
    cur = intervals[0]
        
    for i in range(1, len(intervals)):
        if cur[1] < intervals[i][0]: 
            ans.append(cur)
            cur = intervals[i]
        elif intervals[i][1] >= cur[1]: 
            cur[1] = intervals[i][1]
    ans.append(cur)
    return ans