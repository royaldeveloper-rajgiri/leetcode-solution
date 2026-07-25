---
comments: true
difficulty: 困难
edit_url: https://github.com/royaldeveloper-rajgiri/leetcode-solution/tree/main/solution/3200-3299/3260.Find%20the%20Largest%20Palindrome%20Divisible%20by%20K/README.md
rating: 2370
source: 第 411 场周赛 Q3
tags:
    - 贪心
    - 数学
    - 字符串
    - 动态规划
    - 数论
---

<!-- problem:start -->

# [3260. 找出最大的 N 位 K 回文数](https://leetcode.cn/problems/find-the-largest-palindrome-divisible-by-k)

[English Version](/solution/3200-3299/3260.Find%20the%20Largest%20Palindrome%20Divisible%20by%20K/README_EN.md)

## 题目描述

<!-- description:start -->

<p>给你两个 <strong>正整数</strong> <code>n</code> 和 <code>k</code>。</p>

<p>如果整数 <code>x</code> 满足以下全部条件，则该整数是一个 <strong>k 回文数</strong>：</p>

<ul>
	<li><code>x</code> 是一个 <span data-keyword="palindrome-integer">回文数</span>。</li>
	<li><code>x</code> 可以被 <code>k</code> 整除。</li>
</ul>

<p>以字符串形式返回 <strong>最大的&nbsp;</strong> <code>n</code> 位 <strong>k 回文数</strong>。</p>

<p><strong>注意</strong>，该整数 <strong>不 </strong>含前导零。</p>

<p>&nbsp;</p>

<p><strong class="example">示例 1：</strong></p>

<div class="example-block">
<p><strong>输入：</strong> <span class="example-io">n = 3, k = 5</span></p>

<p><strong>输出：</strong> <span class="example-io">"595"</span></p>

<p><strong>解释：</strong></p>

<p>595 是最大的 3 位 k 回文数。</p>
</div>

<p><strong class="example">示例 2：</strong></p>

<div class="example-block">
<p><strong>输入：</strong> <span class="example-io">n = 1, k = 4</span></p>

<p><strong>输出：</strong> <span class="example-io">"8"</span></p>

<p><strong>解释：</strong></p>

<p>1 位 k 回文数只有 4 和 8。</p>
</div>

<p><strong class="example">示例 3：</strong></p>

<div class="example-block">
<p><strong>输入：</strong> <span class="example-io">n = 5, k = 6</span></p>

<p><strong>输出：</strong> <span class="example-io">"89898"</span></p>
</div>

<p>&nbsp;</p>

<p><strong>提示：</strong></p>

<ul>
	<li><code>1 &lt;= n &lt;= 10<sup>5</sup></code></li>
	<li><code>1 &lt;= k &lt;= 9</code></li>
</ul>

<!-- description:end -->

## 解法

<!-- solution:start -->

### 方法一

<!-- tabs:start -->

#### Python3

```python
   class Solution:
    def is_divisible_by_7(self,number_str):
        remainder = 0
        for char in number_str:
            digit = int(char)
            remainder = (remainder * 10 + digit) % 7
        return remainder == 0
    def largestPalindrome(self, n: int, k: int) -> str:
        if k == 1: return "9" * n
        if k == 2:
            if n == 1:
                return "8"
            if n == 2:
                return "88"
            return "8" + "9"*(n-2) + "8"
        if k == 3: return "9" * n
        if k == 4:
            if n <= 4:
                return "8" * n
            return "88" + (n - 4)*"9" + "88"
        if k == 5:
            if n == 1:
                return "5"
            if n == 2:
                return "55"
            return "5" + (n - 2)*"9" + "5"
        if k == 6:
            if n <= 2:
                return "6" * n
            if n == 3:
                return "888"
            if n % 2 == 1:
                return "8" + ((n - 3)//2)*"9" + "8" + ((n - 3)//2)*"9" + "8"
            if n % 2 == 0:
                return "8" + ((n - 3) // 2) * "9" + "77" + ((n - 3) // 2) * "9" + "8"
        if k == 7:
            if n <= 2:
                return "7" * n
            if n % 2 == 1:
                nines = n // 2
                half = nines * "9"
                for i in range(9, -1, -1):
                    X = half + str(i) + half
                    if self.is_divisible_by_7(X): return X
            if n % 2 == 0:
                nines = (n // 2) - 1
                half = nines * "9"
                for i in range(9, -1, -1):
                    X = half + str(i)*2 + half
                    if self.is_divisible_by_7(X): return X
        if k == 8:
            if n <= 6: return "8" * n
            return "888" + (n - 6) * "9" + "888"
        if k == 9: return "9" *n
```

#### Java

```java
   class Solution {
    StringBuilder sb = new StringBuilder();
    public String largestPalindrome(int n, int k) {
        if (k == 1 || k == 3 || k == 9) {
            return case139(n);
        }
        if (k == 2) {
            return case2(n);
        }
        if (k == 4) {
            return case4(n);
        }
        if (k == 5) {
            return case5(n);
        }
        if (k == 6) {
            return case6(n);
        }
        if (k == 8) {
            return case8(n);
        }
        return case7(n);
    }

    public String case139(int n) {
        while (n > 0) {
            n--;
            sb.append('9');
        }
        return sb.toString();
    }

    public String case2(int n) {
        if (n == 1)
            return "8";
        if (n == 2)
            return "88";
        return "8" + case139(n - 2) + "8";
    }

    public String case4(int n) {
        if (n == 1)
            return "8";
        if (n == 2)
            return "88";
        if (n == 3)
            return "888";
        if (n == 4)
            return "8888";
        return "88" + case139(n - 4) + "88";
    }

    public String case8(int n) {
        if (n <= 6) {
            while (n > 0) {
                sb.append("8");
                n--;
            }
            return sb.toString();
        }
        return "888" + case139(n - 6) + "888";
    }

    public String case5(int n) {
        if (n == 1)
            return "5";
        if (n == 2)
            return "55";
        return "5" + case139(n - 2) + "5";
    }

    public String case6(int n) {
        if (n == 1)
            return "6";
        if (n == 2)
            return "66";
        String s = case2(n);
        if (n % 2 == 0) {
            return s.substring(0, n / 2 - 1) + "77" + s.substring(n / 2 + 1, n);
        }
        return s.substring(0, n / 2) + "8" + s.substring(n / 2 + 1, n);
    }

    public String case7(int n) {
        if (n == 1)
            return "7";
        if (n == 2)
            return "77";
        String s = case139(n);
        if (n % 2 == 0) {
            for (int i = 9; i >= 0; i--) {
                s = s.substring(0, n / 2 - 1) + i + "" + i + s.substring(n / 2 + 1, n);
                int remainder = 0;
                for (int j = 0; j < n; j++)
                    remainder = (remainder * 10 + s.charAt(j) - '0') % 7;
                if (remainder == 0)
                    return s;
            }
            return s;
        }
        for (int i = 9; i >= 0; i--) {
            s = s.substring(0, n / 2) + i + s.substring(n / 2 + 1, n);
            int remainder = 0;
            for (int j = 0; j < n; j++)
                remainder = (remainder * 10 + s.charAt(j) - '0') % 7;
            if (remainder == 0)
                return s;
        }
        return s;
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
