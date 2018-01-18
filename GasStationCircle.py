class Solution:
    def canCompleteCircuit(self, gas, cost):
        """
        :type gas: List[int]
        :type cost: List[int]
        :rtype: int
        """
        start = 0
        curr_pos = 0
        gas_level = 0

        while curr_pos < len(gas):
            gas_level = gas_level + gas[curr_pos] - cost[curr_pos]
            if curr_pos == len(gas) - 1:
                if gas_level < 0:
                    return -1
                else:
                    break
            if gas_level >= 0:
                curr_pos += 1
            else:
                if start == curr_pos:
                    start += 1
                    gas_level = 0
                    curr_pos += 1
                else:
                    start = curr_pos
                    gas_level = 0
                    curr_pos = curr_pos

        # print("AFTER FIRST LOOP: " + str(gas_level))
        if start == 0:
            return 0
        else:
            curr_pos = 0
            while gas_level >= 0 and curr_pos < start:
                # print("GAS: " + str(gas_level) + " POS: " + str(curr_pos))
                # print()
                gas_level = gas_level + gas[curr_pos] - cost[curr_pos]
                if gas_level >= 0:
                    curr_pos += 1

            if curr_pos >= start:
                return start
            else:
                return -1

s = Solution()
print(s.canCompleteCircuit([1,2,3,3],
[2,1,5,1]))






