class Solution:
    def countUnguarded(self, m: int, n: int, guards: List[List[int]], walls: List[List[int]]) -> int:
        directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
        guarded = set()
        guard_set = set(tuple(g) for g in guards)
        wall_set = set(tuple(w) for w in walls)

        for guard_x, guard_y in guards:
            for dx, dy in directions:
                x = guard_x
                y = guard_y
                while (0 <= x + dx < m) and (0 <= y + dy < n) and (tuple([x + dx, y + dy]) not in wall_set) and (tuple([x + dx, y + dy]) not in guard_set):
                    guarded.add(tuple([x + dx, y + dy]))
                    x += dx
                    y += dy

        return m * n - len(guard_set) - len(wall_set) - len(guarded)