# deadends = ["0201","0101","0102","1212","2002"], target = "0202"

def openLock(deadends, target):
    def possible_neighbors(lock_str, deadends):
        if lock_str in deadends:
            return []

        lock_arr = list(lock_str)
        nbrs = []

        for i,c in enumerate(lock_arr):
            int_c = int(c)
            left_turn = str(9) if int_c == 0 else str(int_c - 1)
            right_turn = str((int_c + 1) % 10)

            left_lock = list(lock_str)
            left_lock[i] = left_turn
            right_lock = list(lock_str)
            right_lock[i] = right_turn

            nbrs.append("".join(left_lock))
            nbrs.append("".join(right_lock))
        return nbrs

    visited = set()
    frontier = set(["0000"])
    deadends = set(deadends)
    level = 0

    while frontier:
        new_frontier = set()
        for node_i in frontier:
            curr_nbrs = possible_neighbors(node_i, deadends)
            for nbr in curr_nbrs:
                if nbr in visited:
                    pass
                elif nbr == target:
                    return level + 1
                else:
                    new_frontier.update([nbr])
            visited.update([node_i])

        level += 1
        frontier = new_frontier

    return -1



# print(openLock(["0201","0101","0102","1212","2002"], "0202"))
print(openLock( ["8887","8889","8878","8898","8788","8988","7888","9888"],"8888"))