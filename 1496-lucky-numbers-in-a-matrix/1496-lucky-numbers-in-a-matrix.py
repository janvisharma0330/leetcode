class Solution:
    def luckyNumbers (self, matrix: List[List[int]]) -> List[int]:
        min_row=set()
        max_col=set()
        for r in matrix:
            min_row.add(min(r))
        for c in range(len(matrix[0])):
            maxi=float('-inf')
            for r in range(len(matrix)):
                if matrix[r][c] > maxi:
                    maxi = matrix[r][c]
            max_col.add(maxi)
        return ((min_row)&(max_col)) 

        
        
        