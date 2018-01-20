#  There are a total of n courses you have to take, labeled from 0 to n - 1.
#
# Some courses may have prerequisites, for example to take course 0 you have to first take course 1, which is expressed as a pair: [0,1]
#
# Given the total number of courses and a list of prerequisite pairs, is it possible for you to finish all courses?
import heapq

class Solution:
    def canFinish(self, numCourses, prerequisites):
        """
        :type numCourses: int
        :type prerequisites: List[List[int]]
        :rtype: bool
        """

        unmarked = set([x for x in range(numCourses)])
        adj_list = {}

        for edge in prerequisites:
            id = edge[0]
            req = edge[1]
            if req in adj_list:
                adj_list[req].add(id)
            else:
                adj_list[req] = set([id])

        while unmarked:
            curr = unmarked.pop()
            visit(curr)

        return True

s = Solution()
print(s.canFinish(2,[[0,1]]))