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
