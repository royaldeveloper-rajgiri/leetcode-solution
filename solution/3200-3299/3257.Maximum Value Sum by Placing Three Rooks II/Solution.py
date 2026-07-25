class Solution:
    def maximumValueSum(self, A: List[List[int]]) -> int:
        R, C = len(A), len(A[0])

        rows = [nlargest(3, [(A[r][c], c) for c in range(C)]) for r in range(R)]
        
        def process(rows):
            ans = []  # ans[r] = top 3 choices for A[..r]
            best = []
            for row in rows:
                best.extend(row)
                best.sort(reverse=True)
                nbest = []
                for v, c in best:
                    if all(c != c0 for v0, c0 in nbest):
                        nbest.append((v, c))
                best = nbest[:3]
                ans.append(best[:])
            return ans
        
        pre = process(rows)
        suf = process(rows[::-1])[::-1]

        ans = -inf
        for r in range(1, R - 1):  # r2
            for v1, c1 in pre[r-1]:
                for v2, c2 in rows[r]:
                    for v3, c3 in suf[r+1]:
                        if c1 != c2 != c3 != c1:
                            ans = max(ans, v1 + v2 + v3)
        return ans
