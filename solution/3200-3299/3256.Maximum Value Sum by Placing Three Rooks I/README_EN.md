---
comments: true
difficulty: Hard
edit_url: https://github.com/royaldeveloper-rajgiri/leetcode-solution/tree/main/solution/3200-3299/3256.Maximum%20Value%20Sum%20by%20Placing%20Three%20Rooks%20I/README_EN.md
rating: 2262
source: Biweekly Contest 137 Q3
tags:
    - Array
    - Dynamic Programming
    - Enumeration
    - Matrix
---

<!-- problem:start -->

# [3256. Maximum Value Sum by Placing Three Rooks I](https://leetcode.com/problems/maximum-value-sum-by-placing-three-rooks-i)

[中文文档](/solution/3200-3299/3256.Maximum%20Value%20Sum%20by%20Placing%20Three%20Rooks%20I/README.md)

## Description

<!-- description:start -->

<p>You are given a <code>m x n</code> 2D array <code>board</code> representing a chessboard, where <code>board[i][j]</code> represents the <strong>value</strong> of the cell <code>(i, j)</code>.</p>

<p>Rooks in the <strong>same</strong> row or column <strong>attack</strong> each other. You need to place <em>three</em> rooks on the chessboard such that the rooks <strong>do not</strong> <strong>attack</strong> each other.</p>

<p>Return the <strong>maximum</strong> sum of the cell <strong>values</strong> on which the rooks are placed.</p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>

<div class="example-block">
<p><strong>Input:</strong> <span class="example-io">board = </span>[[-3,1,1,1],[-3,1,-3,1],[-3,2,1,1]]</p>

<p><strong>Output:</strong> 4</p>

<p><strong>Explanation:</strong></p>

<p><img alt="" src="https://fastly.jsdelivr.net/gh/doocs/leetcode@main/solution/3200-3299/3256.Maximum%20Value%20Sum%20by%20Placing%20Three%20Rooks%20I/images/rooks2.png" style="width: 294px; height: 450px;" /></p>

<p>We can place the rooks in the cells <code>(0, 2)</code>, <code>(1, 3)</code>, and <code>(2, 1)</code> for a sum of <code>1 + 1 + 2 = 4</code>.</p>
</div>

<p><strong class="example">Example 2:</strong></p>

<div class="example-block">
<p><strong>Input:</strong> <span class="example-io">board = [[1,2,3],[4,5,6],[7,8,9]]</span></p>

<p><strong>Output:</strong> <span class="example-io">15</span></p>

<p><strong>Explanation:</strong></p>

<p>We can place the rooks in the cells <code>(0, 0)</code>, <code>(1, 1)</code>, and <code>(2, 2)</code> for a sum of <code>1 + 5 + 9 = 15</code>.</p>
</div>

<p><strong class="example">Example 3:</strong></p>

<div class="example-block">
<p><strong>Input:</strong> <span class="example-io">board = [[1,1,1],[1,1,1],[1,1,1]]</span></p>

<p><strong>Output:</strong> <span class="example-io">3</span></p>

<p><strong>Explanation:</strong></p>

<p>We can place the rooks in the cells <code>(0, 2)</code>, <code>(1, 1)</code>, and <code>(2, 0)</code> for a sum of <code>1 + 1 + 1 = 3</code>.</p>
</div>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>3 &lt;= m == board.length &lt;= 100</code></li>
	<li><code>3 &lt;= n == board[i].length &lt;= 100</code></li>
	<li><code>-10<sup>9</sup> &lt;= board[i][j] &lt;= 10<sup>9</sup></code></li>
</ul>

<!-- description:end -->

## Solutions

<!-- solution:start -->

### Solution 1

<!-- tabs:start -->

#### Python3

```python

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
