class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        if not heights:
            return []

        rows, cols = len(heights), len(heights[0])
        pacific = set()
        atlantic = set()

        def dfs(i, j, visited):
            visited.add((i, j))
            for di, dj in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
                ni, nj = i + di, j + dj
                
                if 0 <= ni < rows and 0 <= nj < cols:
                    if (ni, nj) not in visited:
                        if heights[ni][nj] >= heights[i][j]:
                            dfs(ni, nj, visited)
        
        for j in range(cols):
            dfs(0, j, pacific)
        for i in range(rows):
            dfs(i, 0, pacific)

        for j in range(cols):
            dfs(rows - 1, j, atlantic)
        for i in range(rows):
            dfs(i, cols - 1, atlantic)

        return [list(cell) for cell in (pacific & atlantic)]