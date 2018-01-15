class Solution:
    def fourSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[List[int]]
        """

        def twoSum(A, l, r, x):
            result = set()
            while l < r:
                currCand = A[l] + A[r]
                if currCand == x:
                    result.add((A[l], A[r]))
                    l = l + 1
                elif currCand < x:
                    l = l + 1
                else:
                    r = r - 1
            return result

        def threeSum(A, l, r, x):
            result = set()
            for i in range(l, r - 2):
                two_pairs = twoSum(A, i + 1, r - 1, x - A[i])
                for pair in two_pairs:
                    triplet = [x for x in pair]
                    triplet.append(A[i])
                    result.add(tuple(triplet))
            return result

        result = []
        nums = sorted(nums)
        for i in range(len(nums) - 3):
            if i > 0 and nums[i] == nums[i - 1]:
                continue
            else:
                triplets = threeSum(nums, i + 1, len(nums), target - nums[i])
                triplets = [[x for x in triplet] for triplet in triplets]
                for triplet in triplets:
                    triplet.append(nums[i])
                    result.append(triplet)
        return result

s = Solution()
print(s.fourSum([1, 0, -1, 0, -2, 2], 0))


