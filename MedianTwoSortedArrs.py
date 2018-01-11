class Solution:
    def findMedianSortedArrays(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """


        def bin_search(arr, x):
            l = 0
            r = len(arr) - 1
            m = arr[(l+r)//2]
            cand = -1

            while r >= l:
                if arr[m] < x:
                    cand = m
                    l = m + 1
                elif arr[m] == x:
                    cand = m
                    r = m - 1
                else:
                    r = m -1

            return cand

        #simple case. no overlap of two arrays

        l1 = len(nums1)
        l2 = len(nums2)
        if (l1+l2)%2 == 0:
            even = True
            mid = (l1+l2)/2 -1
        else:
            even = False
            mid = (l1+l2)//2

        if l1 == 1 and l2 == 1:
            return (nums1[0] + nums2[0]) / 2

        smaller = None
        if nums1[-1] < nums2[0]:
            smaller = nums1
            larger = nums2
        elif nums2[-1] < nums1[0]:
            smaller = nums2
            larger = nums1

        if smaller != None:
            if even:
                if mid < len(smaller) - 1:
                    return (smaller[mid] + smaller[mid + 1])/2
                else:
                    mid = mid - len(smaller)
                    return (larger[mid], larger[mid + 1])/2
            else:
                if mid < len(smaller) - 1:
                    return smaller[mid]/2
                else:
                    mid = mid - len(smaller)
                    return larger[mid]

        #overlapping case
        

a = [1,3,7]
b=[2,4,6]

c = [1,3]
d = [2,4,6]
x = Solution()
x.findMedianSortedArrays(a,b)
x.findMedianSortedArrays(c,d)