class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        count = 0
        visited = set()
        def dfs(r, c):
            if (r < 0 or r >= len(grid) or c < 0 or c >= len(grid[0]) 
            or (r, c) in visited or grid[r][c] == '0'):
                return

            visited.add((r, c))
            
            dfs(r+1, c)
            dfs(r-1, c)
            dfs(r, c+1)
            dfs(r, c-1)

           

       
        for r in range(len(grid)):
            for c in range(len(grid[0])):
                if grid[r][c] == '1' and (r, c) not in visited:
                    count+=1
                dfs(r, c)
              

        return count
        