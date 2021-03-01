class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        def water(i: int,  j: int):
            if i < 0 or i >= len(grid) or j < 0 or j >= len(grid[0]) or grid[i][j] == '0':
                return
            grid[i][j] = '0'
            water(i+1, j)
            water(i-1, j)
            water(i, j+1)
            water(i, j-1)
        count = 0
        for i in range(len(grid)):
            for j in range(len(grid[i])):
                if grid[i][j] == '1':
                    count += 1
                    water(i, j)
        
        return count