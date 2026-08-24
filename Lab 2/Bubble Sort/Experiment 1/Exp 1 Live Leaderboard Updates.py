def insert_updated_score(board, new_score):
    updated_board = board.copy()
    i = len(updated_board) - 1
    shifts = 0
    while i >= 0 and updated_board[i] < new_score:
        if i + 1 < len(updated_board):
            updated_board[i + 1] = updated_board[i]
        else:
            updated_board.append(updated_board[i])

        shifts += 1
        i -= 1
    if i + 1 < len(updated_board):
        updated_board[i + 1] = new_score
    else:
        updated_board.append(new_score)

    return updated_board, shifts
board = [980, 875, 760, 690, 500]
updated_board, shifts = insert_updated_score(board, 820)
assert updated_board == [980, 875, 820, 760, 690, 500]
board2 = [980, 875, 760, 690, 500]
updated_board2, shifts2 = insert_updated_score(board2, 100)
assert updated_board2[-1] == 100 and shifts2 == 0
print("All test cases passed!")
print("Updated leaderboard:", updated_board)
print("Number of shifts:", shifts)
