class Solution:
    def maxPathLength(self, A, K):
        def LIS(points):
            dp = []
            for y in points:
                i = bisect_left(dp, y)
                if i >= len(dp):
                    dp.append(0)
                dp[i] = y
            return len(dp)

        X, Y = A.pop(K)
        A.sort(key=lambda p: (p[0], -p[1]))
        ans = LIS(y for x, y in A if x<X and y<Y)
        ans += LIS(y for x, y in A if x>X and y>Y)
        return ans + 1
