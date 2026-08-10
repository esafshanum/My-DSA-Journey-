class Solution(object):
    def combinationSum(self, candidates, target):
        candidates.sort()
        result = []

        def backtrack(start, target, path):
            if target == 0:
                result.append(path[:])
                return

            for i in range(start, len(candidates)):
                num = candidates[i]

                if num > target:
                    break

                path.append(num)
                backtrack(i, target - num, path)
                path.pop()

        backtrack(0, target, [])
        return result