class Solution:
    def maximumValueSum(self, board: List[List[int]]) -> int:

        def top3(arr):
            return sorted(range(len(arr)),key = lambda i:-arr[i])

        
        mx = -100000000000
        seen = []
        tops = []
        for row in board:
            tops.append(top3(row))

        def recur(i,cur):
            nonlocal mx
            if len(seen) == 3:
                mx = max(mx,cur)
                return
            if i==len(board):
                return
            recur(i+1,cur)
            for top in tops[i]:
                if top not in seen:
                    seen.append(top)
                    recur(i+1,cur+board[i][top])
                    seen.pop()
        
        recur(0,0)
        return mx
