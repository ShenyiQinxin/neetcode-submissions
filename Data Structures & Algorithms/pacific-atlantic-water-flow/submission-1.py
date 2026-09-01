class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        res = []
        p_visited, a_visited = set(), set()
        rows, cols = len(heights), len(heights[0])

        def dfs(r, c, pre_height, visited):
            if (
                r<0 or r>=rows or c<0 or c>=cols or 
                (r,c) in visited or pre_height > heights[r][c]
            ):
                return
            visited.add((r,c))
            dfs(r-1, c, heights[r][c], visited)
            dfs(r+1, c, heights[r][c], visited)
            dfs(r, c-1, heights[r][c], visited)
            dfs(r, c+1, heights[r][c], visited)
            

        for c in range(cols):
            dfs(0, c, heights[0][c], p_visited)

        for r in range(rows):
            dfs(r, 0, heights[r][0], p_visited)   

        for c in range(cols):
            dfs(rows-1, c, heights[rows-1][c], a_visited)

        for r in range(rows):
            dfs(r, cols-1, heights[rows-1][c] if False else heights[r][cols-1], a_visited)

        for r in range(rows):
            for c in range(cols):
                if (r, c) in p_visited and (r, c) in a_visited:
                    res.append([r,c])


        return res





        