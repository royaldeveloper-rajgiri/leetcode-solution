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
