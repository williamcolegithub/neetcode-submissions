class Solution:
    def longestPalindrome(self, s: str) -> str:
        rev = s[::-1]
        n = len(s)
        
        dp = [[0] * (n + 1) for _ in range(n + 1)]
        
        max_len = 0
        end_idx = 0
        
        for i in range(1, n + 1):
            for j in range(1, n + 1):
                if s[i - 1] == rev[j - 1]:
                    dp[i][j] = dp[i - 1][j - 1] + 1
                    if dp[i][j] > max_len:
                        original_idx = n - j
                        if original_idx == i - dp[i][j]:
                            max_len = dp[i][j]
                            end_idx = i
                else:
                    dp[i][j] = 0
        
        return s[end_idx - max_len:end_idx]