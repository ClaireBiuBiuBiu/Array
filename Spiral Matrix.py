'''
Given a matrix of m x n elements (m rows, n columns), return all elements of the matrix in spiral order.
Approach 1: Simulation
Intuition

Draw the path that the spiral makes. We know that the path should turn clockwise whenever it would go out of bounds or into a cell that was previously visited.

Algorithm

Let the array have \text{R}R rows and \text{C}C columns. \text{seen[r][c]}seen[r][c] denotes that the cell on the\text{r}r-th row and \text{c}c-th column was previously visited. Our current position is \text{(r, c)}(r, c), facing direction \text{di}di, and we want to visit \text{R}R x \text{C}C total cells.

As we move through the matrix, our candidate next position is \text{(cr, cc)}(cr, cc). If the candidate is in the bounds of the matrix and unseen, then it becomes our next position; otherwise, our next position is the one after performing a clockwise turn.

'''
class Solution(object):
    def spiralOrder(self, matrix):
        if not matrix: return []
        R, C = len(matrix), len(matrix[0])
        seen = [[False] * C for _ in matrix]
        ans = []
        dr = [0, 1, 0, -1]
        dc = [1, 0, -1, 0]
        r = c = di = 0
        for _ in range(R * C):
            ans.append(matrix[r][c])
            seen[r][c] = True
            cr, cc = r + dr[di], c + dc[di]
            if 0 <= cr < R and 0 <= cc < C and not seen[cr][cc]:
                r, c = cr, cc
            else:
                di = (di + 1) % 4
                r, c = r + dr[di], c + dc[di]
        return ans