class Solution:
    def longestPalindrome(self, s: str) -> str:
        n = len(s)
        base = 31
        mod = 10**9 + 7
        
        # Precompute forward and reverse hashes
        fwd = [0] * (n + 1)
        rev = [0] * (n + 1)
        power = [1] * (n + 1)
        
        for i in range(n):
            fwd[i + 1] = (fwd[i] * base + ord(s[i])) % mod
            rev[i + 1] = (rev[i] * base + ord(s[n - 1 - i])) % mod
            power[i + 1] = (power[i] * base) % mod
        
        def get_fwd_hash(l, r):
            return (fwd[r + 1] - fwd[l] * power[r - l + 1]) % mod
        
        def get_rev_hash(l, r):
            rl = n - 1 - r
            rr = n - 1 - l
            return (rev[rr + 1] - rev[rl] * power[rr - rl + 1]) % mod
        
        res_start, res_len = 0, 1
        
        for center in range(n):
            # Odd length
            lo, hi = 0, min(center, n - 1 - center)
            while lo <= hi:
                mid = (lo + hi) // 2
                if get_fwd_hash(center - mid, center + mid) == get_rev_hash(center - mid, center + mid):
                    if 2 * mid + 1 > res_len:
                        res_len = 2 * mid + 1
                        res_start = center - mid
                    lo = mid + 1
                else:
                    hi = mid - 1
            
            # Even length
            lo, hi = 0, min(center, n - 2 - center)
            while lo <= hi:
                mid = (lo + hi) // 2
                if get_fwd_hash(center - mid, center + 1 + mid) == get_rev_hash(center - mid, center + 1 + mid):
                    if 2 * mid + 2 > res_len:
                        res_len = 2 * mid + 2
                        res_start = center - mid
                    lo = mid + 1
                else:
                    hi = mid - 1
        
        return s[res_start:res_start + res_len]