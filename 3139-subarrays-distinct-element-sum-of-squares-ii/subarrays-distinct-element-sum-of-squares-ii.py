
class Solution(object):
    def sumCounts(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        MOD = 10**9 + 7
        n = len(nums)

        total = [0] * (4 * n)
        squares = [0] * (4 * n)
        lazy = [0] * (4 * n)

        last = {}
        ans = 0

        def apply(node, l, r, val):
            length = r - l + 1

            squares[node] = (
                squares[node]
                + 2 * val * total[node]
                + length * val * val
            ) % MOD

            total[node] = (total[node] + length * val) % MOD
            lazy[node] += val

        def push(node, l, r):
            if lazy[node] == 0 or l == r:
                return

            mid = (l + r) // 2
            val = lazy[node]

            apply(node * 2, l, mid, val)
            apply(node * 2 + 1, mid + 1, r, val)

            lazy[node] = 0

        def update(node, l, r, ql, qr, val):
            if ql > r or qr < l:
                return

            if ql <= l and r <= qr:
                apply(node, l, r, val)
                return

            push(node, l, r)

            mid = (l + r) // 2

            update(node * 2, l, mid, ql, qr, val)
            update(node * 2 + 1, mid + 1, r, ql, qr, val)

            total[node] = (
                total[node * 2] + total[node * 2 + 1]
            ) % MOD

            squares[node] = (
                squares[node * 2] + squares[node * 2 + 1]
            ) % MOD

        for i, num in enumerate(nums):
            left = last.get(num, -1) + 1

            update(1, 0, n - 1, left, i, 1)

            ans = (ans + squares[1]) % MOD
            last[num] = i

        return ans
