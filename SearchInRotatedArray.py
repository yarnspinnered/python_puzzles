class Solution:
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        if len(nums) == 0:
            return -1

        def bin_search(A, l, r, x):
            while l <= r:
                m = (l + r) // 2
                if A[m] == x:
                    return m
                elif A[m] < x:
                    l = m + 1
                else:
                    r = m - 1
            return -1

        l = 0
        r = len(nums) - 1
        pivot = 0

        while l <= r:
            pivot = (l + r) // 2
            if l == r:
                break
            elif r == l + 1:
                if nums[r] < nums[l]:
                    pivot = r
                break
            if nums[l] < nums[pivot]:
                l = pivot
            else:
                r = pivot

        print(pivot)
        result = max(bin_search(nums, 0, pivot - 1, target),
                     bin_search(nums, pivot, len(nums) - 1, target))

        return result

s = Solution()
print(s.search([5,1,2,3,4], 3))