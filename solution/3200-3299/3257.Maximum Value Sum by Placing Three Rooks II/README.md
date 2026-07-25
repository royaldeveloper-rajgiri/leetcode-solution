---
comments: true
difficulty: 困难
edit_url: https://github.com/royaldeveloper-rajgiri/leetcode-solution/tree/main/solution/3200-3299/3257.Maximum%20Value%20Sum%20by%20Placing%20Three%20Rooks%20II/README.md
rating: 2553
source: 第 137 场双周赛 Q4
tags:
    - 数组
    - 动态规划
    - 枚举
    - 矩阵
---

<!-- problem:start -->

# [3257. 放三个车的价值之和最大 II](https://leetcode.cn/problems/maximum-value-sum-by-placing-three-rooks-ii)

[English Version](/solution/3200-3299/3257.Maximum%20Value%20Sum%20by%20Placing%20Three%20Rooks%20II/README_EN.md)

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

<p><img alt="" src="https://fastly.jsdelivr.net/gh/doocs/leetcode@main/solution/3200-3299/3257.Maximum%20Value%20Sum%20by%20Placing%20Three%20Rooks%20II/images/rooks2.png" style="width: 294px; height: 450px;" /></p>

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
	<li><code>3 &lt;= m == board.length &lt;= 500</code></li>
	<li><code>3 &lt;= n == board[i].length &lt;= 500</code></li>
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
```

#### Java

```java
   class Solution {
    class Cell {
        int i;
        int j;
        int val;
        
        public Cell(int i, int j, int val) {
            this.i = i;
            this.j = j;
            this.val = val;
        }
    }
    
    public long maximumValueSum(int[][] board) {
        int rows = board.length;
        int cols = board[0].length;
        
        //Step 1: Prepare Cell List with at most 3 cells per row
        List<Cell> cellList = new ArrayList<>();
        for (int i = 0; i < rows; i++) {
            PriorityQueue<Cell> minHeap = new PriorityQueue<>((a, b) -> a.val - b.val);
            for (int j = 0; j < cols; j++) {
                minHeap.offer(new Cell(i, j, board[i][j]));
                if (minHeap.size() > 3) {
                    minHeap.poll();
                }
            }
            
            while (!minHeap.isEmpty()) {
                cellList.add(minHeap.poll());
            }
        }
        
        //Step 2: Prepare Cell List with at most 3 cells per column
        Collections.sort(cellList, (a, b) -> b.val - a.val);
        List<Cell> filteredList = new ArrayList<>();
        Map<Integer, Integer> columnCount = new HashMap<>();
        for (Cell cell : cellList) {
            int j = cell.j;
            if (columnCount.getOrDefault(j, 0) < 3) {
                filteredList.add(cell);
                columnCount.put(j, columnCount.getOrDefault(j, 0) + 1);
            }
        }
        
        //Step 3: Final ans
        long ans = Long.MIN_VALUE;
        for (int i = 0; i < Math.min(filteredList.size(), 15); i++) {
            for (int j = i+1; j < Math.min(filteredList.size(), 15); j++) {
                for (int k = j+1; k < Math.min(filteredList.size(), 15); k++) {
                    Cell cellI = filteredList.get(i);
                    Cell cellJ = filteredList.get(j);
                    Cell cellK = filteredList.get(k);
                    
                    if (cellI.i == cellJ.i || cellI.i == cellK.i || cellJ.i == cellK.i ||
                       cellI.j == cellJ.j || cellI.j == cellK.j || cellJ.j == cellK.j) {
                        continue;
                    }
                    
                    ans = Math.max(ans, 0L + cellI.val + cellJ.val + cellK.val);
                }
            }
        }
        
        return ans;
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
