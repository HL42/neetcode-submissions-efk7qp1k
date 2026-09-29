class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        rows = [set() for _ in range(9)]
        cols = [set() for _ in range(9)]
        boxs = [set() for _ in range(9)]

        for r in range(9):
            for c in range(9):
                value = board[r][c]

                if value == ".":
                    continue;

                box_num = (r // 3) * 3 + (c // 3) 

                if value in rows[r]:
                    return False

                rows[r].add(value)

                if value in cols[c]:
                    return False
                
                cols[c].add(value)

                if value in boxs[box_num]:
                    return False

                boxs[box_num].add(value)

        return True

                
            

        