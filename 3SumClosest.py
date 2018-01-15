class Solution:
    def threeSumClosest(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        def twoSumClosest(A, l, r, x):
            bestCand = A[l] + A[l + 1]
            while l < r:
                currCand = A[l] + A[r]
                if abs(currCand - x) < abs(bestCand - x):
                    bestCand = currCand
                if currCand == x:
                    return currCand
                elif currCand < x:
                    l = l + 1
                else:
                    r = r - 1
            return bestCand

        nums = sorted(nums)
        bestCand = sum(nums[:3])
        for i in range(len(nums) - 2):
            val_i = nums[i]
            newCand = val_i + twoSumClosest(nums, i + 1, len(nums) - 1, target - val_i)
            if abs(newCand - target) < abs(bestCand - target):
                bestCand = newCand

        return bestCand

s = Solution()
print(s.threeSumClosest([-1,2,1,-4],1))
