class Solution(object):
    def countVowelPermutation(self, n):
        """
        :type n: int
        :rtype: int
        """
        MOD = 10**9 + 7
        
        # Base case for length 1: each vowel appears once
        a, e, i, o, u = 1, 1, 1, 1, 1
        
        for _ in range(n - 1):
            a_next = (e + i + u) % MOD
            e_next = (a + i) % MOD
            i_next = (e + o) % MOD
            o_next = i % MOD
            u_next = (i + o) % MOD
            
            a, e, i, o, u = a_next, e_next, i_next, o_next, u_next
            
        return (a + e + i + o + u) % MOD     