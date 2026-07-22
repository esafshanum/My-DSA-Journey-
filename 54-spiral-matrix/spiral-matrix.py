class Solution(object):
    def spiralOrder(self, matrix):
        if not matrix or not matrix[0]:
            return []

        result = []

        top, left = 0, 0
        bottom, right = len(matrix) - 1, len(matrix[0]) - 1

        while top <= bottom and left <= right:

            # Left to right
            for i in range(left, right + 1):
                result.append(matrix[top][i])
            top += 1

            # Top to bottom
            for i in range(top, bottom + 1):
                result.append(matrix[i][right])
            right -= 1

            # Right to left
            if top <= bottom:
                for i in range(right, left - 1, -1):
                    result.append(matrix[bottom][i])
                bottom -= 1

            # Bottom to top
            if left <= right:
                for i in range(bottom, top - 1, -1):
                    result.append(matrix[i][left])
                left += 1

        return result
        