class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        res = []
        p_visited = set()
        a_visited = set()
        ROWS = len(heights)
        COLS = len(heights[0])
        preHeight = -1

        def dfs(r, c, preHeight, visited):
            print(preHeight)
            if (r < 0 or r >= ROWS or c <0 or c >= COLS or (r, c) in visited or
                preHeight > heights[r][c]):
                return

            if r == 0 or c == 0:
                p_visited.add((r, c))
            
            # res.add((r, c))
            
            visited.add((r, c))
            dfs(r-1, c, heights[r][c], visited)
            dfs(r+1, c, heights[r][c], visited)
            dfs(r, c-1, heights[r][c], visited)
            dfs(r, c+1, heights[r][c], visited)

            
        # Pacific
        for top in range(COLS):
            dfs(0, top, preHeight, p_visited)
            
        for left in range(ROWS):
            dfs(left, 0, preHeight, p_visited)
           
        # Atlantic
        for bottom in range(COLS):
            dfs(ROWS-1, bottom, preHeight, a_visited)
            
        for right in range(ROWS):
            dfs(right, COLS-1, preHeight, a_visited)

        for r in range(ROWS):
            for c in range(COLS):
                if (r, c) in p_visited and (r, c) in a_visited:
                    res.append([r, c])
        return res
        