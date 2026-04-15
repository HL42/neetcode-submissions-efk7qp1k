class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        count = 0
        if not grid:
            return 0

        rows = len(grid)
        cols = len(grid[0])
        
        def sink_island(r, c):
            if r < 0 or c < 0 or r >= rows or c >= cols:
                return

            if grid[r][c] == '0':
                return 

            grid[r][c] = '0'

            sink_island(r - 1, c) 
            sink_island(r + 1, c) 
            sink_island(r, c - 1) 
            sink_island(r, c + 1)

        for r in range(rows):
        
            for c in range(cols):

                if grid[r][c] == '1':

                    count += 1
                    sink_island(r, c)

        return count