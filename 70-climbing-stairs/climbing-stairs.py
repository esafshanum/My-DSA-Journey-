class Solution(object):
    def climbStairs(self, n):
        def multiply(a, b):
            return [
                [
                    a[0][0] * b[0][0] + a[0][1] * b[1][0],
                    a[0][0] * b[0][1] + a[0][1] * b[1][1]
                ],
                [
                    a[1][0] * b[0][0] + a[1][1] * b[1][0],
                    a[1][0] * b[0][1] + a[1][1] * b[1][1]
                ]
            ]

        def power(mat, p):
            result = [[1, 0], [0, 1]]
            while p:
                if p & 1:
                    result = multiply(result, mat)
                mat = multiply(mat, mat)
                p >>= 1
            return result

        if n <= 2:
            return n

        return power([[1, 1], [1, 0]], n)[0][0]