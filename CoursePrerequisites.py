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
        unmarked = [x for x in range(numCourses)]
        temp_marked = [False for x in range(numCourses)]
        marked = [False for x in range(numCourses)]

        def visit(u):
            if marked[u]:
                return True
            if temp_marked[u]:
                return False
            temp_marked[u] = True
            if u in adj_list:
                for nbr in adj_list[u]:
                    if not visit(nbr): return False
            marked[u] = True
            res.insert(0, u)
            return True

        adj_list = {}
        res = []

        for edge in prerequisites:
            id = edge[0]
            req = edge[1]
            if req in adj_list:
                adj_list[req].add(id)
            else:
                adj_list[req] = set([id])

        while unmarked:
            curr = unmarked.pop()
            if not visit(curr):
                return False


        return True

s = Solution()
