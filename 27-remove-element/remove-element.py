class Solution(object):
    def removeElement(self, nums, val):
        n = len(nums)
        l = 0
        r = n-1
        count = 0
        while l<=r:
            if nums[r] == val:
                r-=1
            elif nums[l] != val :
                l+=1
                count+=1
            else:
                nums[l],nums[r] = nums[r],nums[l]
                l+=1
                r-=1
                count+=1
        return count