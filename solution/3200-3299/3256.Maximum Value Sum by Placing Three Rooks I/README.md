---
comments: true
difficulty: 困难
edit_url: https://github.com/royaldeveloper-rajgiri/leetcode-solution/tree/main/solution/3200-3299/3256.Maximum%20Value%20Sum%20by%20Placing%20Three%20Rooks%20I/README.md
rating: 2262
source: 第 137 场双周赛 Q3
tags:
    - 数组
    - 动态规划
    - 枚举
    - 矩阵
---

<!-- problem:start -->

# [3256. 放三个车的价值之和最大 I](https://leetcode.cn/problems/maximum-value-sum-by-placing-three-rooks-i)

[English Version](/solution/3200-3299/3256.Maximum%20Value%20Sum%20by%20Placing%20Three%20Rooks%20I/README_EN.md)

## 题目描述

<!-- description:start -->

<p>给你一个&nbsp;<code>m x n</code>&nbsp;的二维整数数组&nbsp;<code>board</code>&nbsp;，它表示一个国际象棋棋盘，其中&nbsp;<code>board[i][j]</code>&nbsp;表示格子 <code>(i, j)</code>&nbsp;的 <strong>价值</strong>&nbsp;。</p>

<p>处于 <strong>同一行</strong>&nbsp;或者 <strong>同一列</strong>&nbsp;车会互相 <strong>攻击</strong>&nbsp;。你需要在棋盘上放三个车，确保它们两两之间都&nbsp;<b>无法互相攻击</b>&nbsp;。</p>

<p>请你返回满足上述条件下，三个车所在格子 <strong>值</strong>&nbsp;之和 <strong>最大</strong>&nbsp;为多少。</p>

<p>&nbsp;</p>

<p><strong class="example">示例 1：</strong></p>

<div class="example-block">
<p><span class="example-io"><b>输入：</b>board = </span>[[-3,1,1,1],[-3,1,-3,1],[-3,2,1,1]]</p>

<p><b>输出：</b>4</p>

<p><strong>解释：</strong></p>

<p><img alt="" src="https://fastly.jsdelivr.net/gh/doocs/leetcode@main/solution/3200-3299/3256.Maximum%20Value%20Sum%20by%20Placing%20Three%20Rooks%20I/images/rooks2.png" style="width: 294px; height: 450px;" /></p>

<p>我们可以将车分别放在格子&nbsp;<code>(0, 2)</code>&nbsp;，<code>(1, 3)</code>&nbsp;和&nbsp;<code>(2, 1)</code>&nbsp;处，价值之和为&nbsp;<code>1 + 1 + 2 = 4</code>&nbsp;。</p>
</div>

<p><strong class="example">示例 2：</strong></p>

<div class="example-block">
<p><span class="example-io"><b>输入：</b>board = [[1,2,3],[4,5,6],[7,8,9]]</span></p>

<p><span class="example-io"><b>输出：</b>15</span></p>

<p><strong>解释：</strong></p>

<p>我们可以将车分别放在格子&nbsp;<code>(0, 0)</code>&nbsp;，<code>(1, 1)</code>&nbsp;和&nbsp;<code>(2, 2)</code>&nbsp;处，价值之和为&nbsp;<code>1 + 5 + 9 = 15</code>&nbsp;。</p>
</div>

<p><strong class="example">示例 3：</strong></p>

<div class="example-block">
<p><span class="example-io"><b>输入：</b>board = [[1,1,1],[1,1,1],[1,1,1]]</span></p>

<p><span class="example-io"><b>输出：</b>3</span></p>

<p><strong>解释：</strong></p>

<p>我们可以将车分别放在格子&nbsp;<code>(0, 2)</code>&nbsp;，<code>(1, 1)</code>&nbsp;和&nbsp;<code>(2, 0)</code>&nbsp;处，价值之和为&nbsp;<code>1 + 1 + 1 = 3</code>&nbsp;。</p>
</div>

<p>&nbsp;</p>

<p><strong>提示：</strong></p>

<ul>
	<li><code>3 &lt;= m == board.length &lt;= 100</code></li>
	<li><code>3 &lt;= n == board[i].length &lt;= 100</code></li>
	<li><code>-10<sup>9</sup> &lt;= board[i][j] &lt;= 10<sup>9</sup></code></li>
</ul>

<!-- description:end -->

## 解法

<!-- solution:start -->

### 方法一

<!-- tabs:start -->

#### Python3

```python
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
```

#### Java

```java
class Solution {
    public long max = Long.MIN_VALUE;
    public long maximumValueSum(int[][] board) {
        int m = board.length;
        int n = board[0].length;
        List<List<Integer>> valuesList = new ArrayList<>(m*n);
        //Get max 3 row values for all rows
        for(int i=0; i<m; ++i){
            List<List<Integer>> rowValues = new ArrayList<>(n);
            int max1 = -1;
            int max2 = -1;
            int max3 = -1;
            for(int j=0; j<n; ++j){
                rowValues.add(new ArrayList<Integer>(3));
                List<Integer> value = rowValues.get(rowValues.size()-1);
                value.add(board[i][j]);
                value.add(i);
                value.add(j);
                if(max1 == -1 || board[i][j] >= rowValues.get(max1).get(0)){
                    max3 = max2;
                    max2 = max1;
                    max1 = j;
                }else if(max2 == -1 || board[i][j] >= rowValues.get(max2).get(0)){
                    max3 = max2;
                    max2 = j;
                }else if(max3 == -1 || board[i][j] >= rowValues.get(max3).get(0)){
                    max3 = j;
                }
            }
            valuesList.add(rowValues.get(max1));
            valuesList.add(rowValues.get(max2));
            valuesList.add(rowValues.get(max3));
        }
        //Sort all the possible values
        Collections.sort(valuesList, new Comparator<List<Integer>>(){
            @Override
            public int compare(List<Integer> a, List<Integer> b){
                return b.get(0) - a.get(0);
            }
        });
        boolean[] rows = new boolean[m];
        boolean[] cols = new boolean[n];
        
        backtrack(0, 0, 0, valuesList, rows, cols);

        return max;
    }
    public void backtrack(int idx, long curSum, int nums, List<List<Integer>> valuesList, boolean[] rows, boolean[] cols){
        if(nums == 3){
            if(curSum > max){
                max = curSum;
            }
            return;
        }
        if(idx >= valuesList.size()){
            return;
        }
        long value = valuesList.get(idx).get(0);

        //Check if it is possible to get new max from here. If not, return.
        if(curSum + value * (3 - nums) < max){
            return;
        }

        //Pick
        int row = valuesList.get(idx).get(1);
        int col = valuesList.get(idx).get(2);
        if(!rows[row] && !cols[col]){
            rows[row] = true;
            cols[col] = true;
            backtrack(idx+1, curSum+value, nums+1, valuesList, rows, cols);
            rows[row] = false;
            cols[col] = false;
        }

        //Dont pick
        backtrack(idx+1, curSum, nums, valuesList, rows, cols);

    }
}
```

#### C++

```cpp

```

#### Go

```go

```

<!-- tabs:end -->

<!-- solution:end -->

<!-- problem:end -->
