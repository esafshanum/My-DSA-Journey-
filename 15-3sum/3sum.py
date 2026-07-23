class Solution(object):
    def threeSum(self, nums):
        ans = []
        n = len(nums)
        nums.sort()

        for i in range(n):
            if i != 0 and nums[i] == nums[i - 1]:
                continue

            # moving the 2 pointers
            j = i + 1
            k = n - 1

            while j < k:
                total_sum = nums[i] + nums[j] + nums[k]

                if total_sum < 0:
                    j += 1
                elif total_sum > 0:
                    k -= 1
                else:
                    ans.append([nums[i], nums[j], nums[k]])
                    j += 1

                    while j < k and nums[j] == nums[j - 1]:
                        j += 1

        return ans
        