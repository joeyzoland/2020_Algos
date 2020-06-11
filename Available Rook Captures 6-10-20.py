"""
On an 8 x 8 chessboard, there is one white rook.  There also may be empty squares, white bishops, and black pawns.  These are given as characters 'R', '.', 'B', and 'p' respectively. Uppercase characters represent white pieces, and lowercase characters represent black pieces.

The rook moves as in the rules of Chess: it chooses one of four cardinal directions (north, east, west, and south), then moves in that direction until it chooses to stop, reaches the edge of the board, or captures an opposite colored pawn by moving to the same square it occupies.  Also, rooks cannot move into the same square as other friendly bishops.

Return the number of pawns the rook can capture in one move.



Example 1:



Input: [[".",".",".",".",".",".",".","."],[".",".",".","p",".",".",".","."],[".",".",".","R",".",".",".","p"],[".",".",".",".",".",".",".","."],[".",".",".",".",".",".",".","."],[".",".",".","p",".",".",".","."],[".",".",".",".",".",".",".","."],[".",".",".",".",".",".",".","."]]
Output: 3
Explanation:
In this example the rook is able to capture all the pawns.
"""

class Solution:
    def numRookCaptures(self, board):
        #Find the rook
        #Initialize a pawnCount
        #Search up until you find a pawn, in which case you increment pawnCount
            #If you reach a bishop or the edge of the board, cancel the call
        #Do the same thing for the three other directions
        #Return pawnCount

        rowCount = len(board)
        columnCount = len(board[0])

        rookPosition = None
        for row in range(rowCount):
            for column in range(columnCount):
                if board[row][column] == "R":
                    rookPosition = [row, column]
                    break

        pawnCount = 0

        for y in range(rookPosition[0] - 1, -1, -1):
            if board[y][rookPosition[1]] == "p":
                pawnCount += 1
                break
            elif board[y][rookPosition[1]] == "B":
                break

        for y in range(rookPosition[0] + 1, rowCount):
            if board[y][rookPosition[1]] == "p":
                pawnCount += 1
                break
            elif board[y][rookPosition[1]] == "B":
                break

        for x in range(rookPosition[1] - 1, -1, -1):
            if board[rookPosition[0]][x] == "p":
                pawnCount += 1
                break
            elif board[rookPosition[0]][x] == "B":
                break

        for x in range(rookPosition[1] + 1, columnCount):
            if board[rookPosition[0]][x] == "p":
                pawnCount += 1
                break
            elif board[rookPosition[0]][x] == "B":
                break

        return pawnCount

solution = Solution()
input = [[".",".",".",".",".",".",".","."],[".",".",".","p",".",".",".","."],[".",".",".","R",".",".",".","p"],[".",".",".",".",".",".",".","."],[".",".",".",".",".",".",".","."],[".",".",".","p",".",".",".","."],[".",".",".",".",".",".",".","."],[".",".",".",".",".",".",".","."]]
print (solution.numRookCaptures(input))
