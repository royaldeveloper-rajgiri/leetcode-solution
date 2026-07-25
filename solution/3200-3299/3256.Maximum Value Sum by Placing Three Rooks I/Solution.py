class Solution:
    def maximumValueSum(self, A: List[List[int]]) -> int:
        m, n = len(A), len(A[0])
        ans = float("-inf")
        max_val = [[float("-inf")] * 3 for _ in range(m)]
        max_cols = [[-1] * 3 for _ in range(m)]

        for i in range(m):
            cols = [(A[i][j], j) for j in range(n)]
            cols.sort(reverse=True) 

            for k in range(min(3, n)):
                max_val[i][k] = cols[k][0]
                max_cols[i][k] = cols[k][1]

        for r1 in range(m):
            for r2 in range(r1 + 1, m):
                for r3 in range(r2 + 1, m):
                    for i in range(3):
                        for j in range(3):
                            if max_cols[r2][j] == max_cols[r1][i]:
                                continue
                            for k in range(3):
                                if (max_cols[r3][k] == max_cols[r1][i] or
                                    max_cols[r3][k] == max_cols[r2][j]):
                                    continue

                                current_sum = (max_val[r1][i] +
                                               max_val[r2][j] +
                                               max_val[r3][k])
                                ans = max(ans, current_sum)

        return ans
