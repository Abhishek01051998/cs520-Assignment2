"""
Compute the value brought by a given move by placing a new token for player
at (row, column). The value is the number of opponent pieces getting flipped
by the move. 

A move is valid if for the player, the location specified by (row, column) is
(1) empty and (2) will cause some pieces from the other player to flip. The
return value for the function should be the number of pieces hat will be moved.
If the move is not valid, then the value 0 (zero) should be returned. Note
here that row and column both start with index 0. 
"""


def get_move_value(state, player, row, column):
    flipped = 0
    # Your implementation goes here
    if state[row][column] != ' ':
        return 0
    o_player=''
    if player=='B':
        o_player = 'W'
    else:
        o_player = 'B'
    temp_flip_hold = 0

    #  row 
    if row == 0:
        for i in range(1, len(state)):
            if state[i][column] == o_player:
                temp_flip_hold += 1
            elif state[i][column] == player:
                flipped += temp_flip_hold
                break
            else:
                break
    elif 0 < row < len(state) - 1:
        for i in range(row - 1, -1, -1):
            if state[i][column] == o_player:
                temp_flip_hold += 1
            elif state[i][column] == player:
                flipped += temp_flip_hold
                break
            else:
                break
        temp_flip_hold = 0
        for i in range(row + 1, len(state)):
            if state[i][column] == o_player:
                temp_flip_hold += 1
            elif state[i][column] == player:
                flipped += temp_flip_hold
                break
            else:
                break
    elif row + 1 == len(state):
        for i in range(row - 1, -1, -1):
            if state[i][column] == o_player:
                temp_flip_hold += 1
            elif state[i][column] == player:
                flipped += temp_flip_hold
                break
            else:
                break
    temp_flip_hold = 0

    # column 
    if column == 0:
        for j in range(1, len(state[row])):
            if state[row][j] == o_player:
                temp_flip_hold += 1
            elif state[row][j] == player:
                flipped += temp_flip_hold
                break
            else:
                break
    elif 0 < column < len(state[row]) - 1:
        for j in range(column - 1, -1, -1):
            if state[row][j] == o_player:
                temp_flip_hold += 1
            elif state[row][j] == player:
                flipped += temp_flip_hold
                break
            else:
                break
        temp_flip_hold = 0
        for j in range(column + 1, len(state)):
            if state[row][j] == o_player:
                temp_flip_hold += 1
            elif state[row][j] == player:
                flipped += temp_flip_hold
                break
            else:
                break
    elif column + 1 == len(state[row]):
        for j in range(column - 1, -1, -1):
            if state[row][j] == o_player:
                temp_flip_hold += 1
            elif state[row][j] == player:
                flipped += temp_flip_hold
                break
            else:
                break
    temp_flip_hold = 0

    #  upper right diagonal 
    if row == 0 or column == len(state[row]) - 1:
        y = column + 1
        for i in range(row + 1, y):
            if state[i][column - i] == o_player:
                temp_flip_hold += 1
            elif state[i][column - i] == player:
                flipped += temp_flip_hold
                break
            else:
                break
    elif row == len(state) - 1 or column == 0:
        x = row + 1
        for j in range(column + 1, x):
            if state[row - j][j] == o_player:
                temp_flip_hold += 1
            elif state[row - j][j] == player:
                flipped += temp_flip_hold
                break
            else:
                break
    else:
        i = row + 1
        j = column - 1
        while i != len(state) and j != -1:
            if state[i][j] == o_player:
                temp_flip_hold += 1
                i += 1
                j -= 1
            elif state[i][j] == player:
                flipped += temp_flip_hold
                break
            else:
                break
        temp_flip_hold = 0
        i = row - 1
        j = column + 1
        while i != -1 and j != len(state[row]):
            if state[i][j] == o_player:
                temp_flip_hold += 1
                i -= 1
                j += 1
            elif state[i][j] == player:
                flipped += temp_flip_hold
                break
            else:
                break
    temp_flip_hold = 0

    #  upper left diagonal 
    if row == 0 or column == 0:
        i = row + 1
        j = column + 1
        while i != len(state) and j != len(state[row]):
            if state[i][j] == o_player:
                temp_flip_hold += 1
                i += 1
                j += 1
            elif state[i][j] == player:
                flipped += temp_flip_hold
                break
            else:
                break
    elif row == len(state) - 1 or column == len(state[row]) - 1:
        i = row - 1
        j = column - 1
        while i != -1 and j != -1:
            if state[i][j] == o_player:
                temp_flip_hold += 1
                i -= 1
                j -= 1
            elif state[i][j] == player:
                flipped += temp_flip_hold
                break
            else:
                break
    else:
        i = row - 1
        j = column - 1
        while i != -1 and j != -1:
            if state[i][j] == o_player:
                temp_flip_hold += 1
                i -= 1
                j -= 1
            elif state[i][j] == player:
                flipped += temp_flip_hold
                break
            else:
                break
        temp_flip_hold = 0
        i = row + 1
        j = column + 1
        while i != len(state) and j != len(state[row]):
            if state[i][j] == o_player:
                temp_flip_hold += 1
                i += 1
                j += 1
            elif state[i][j] == player:
                flipped += temp_flip_hold
                break
            else:
                break

    return flipped


"""
Execute a move that updates the state. A new state should be crated. The move
must be valid. Note that the new state should be a clone of the old state and
in particular, should not share memory with the old state. 
"""


def execute_move(state, player, row, column):
    #Making  new state with  number of rows
    new_state = []

    for x in range(0, len(state),1):
        new_state.append([])
        for y in range(0, len(state), 1):
            if x == row and y == column:
                new_state[x].append(player)
            else:
                new_state[x].append(state[x][y])

    #Calc changes caused by move


    #For DOWN
    for x in range(row+1, len(state), 1):
        if new_state[x][column] == ' ':
            break
        if new_state[x][column] != player:
            continue
        if new_state[x][column] == player:
            for change in range(row+1, x, 1):
                new_state[change][column] = player
            break

    #FOR LEFT
    for y in range(column+1, len(state), 1):
        if new_state[row][y] == ' ':
            break
        if new_state[row][y] != player:
            continue
        if new_state[row][y] == player:
            for change in range(column+1, y, 1):
                new_state[row][change] = player
            break
    #FOR UP
    for x in range(row - 1, -1, -1):
        if new_state[x][column] == ' ':
            break
        if new_state[x][column] != player:
            continue
        if new_state[x][column] == player:
            for change in range(row-1, x, -1):
                new_state[change][column] = player
            break

    #FOR RIGHT
    for y in range(column-1, -1, -1):
        if new_state[row][y] == ' ':
            break
        if new_state[row][y] != player:
            continue
        if new_state[row][y] == player:
            for c in range(column-1, y, -1):
                new_state[row][c] = player
            break


    #FOR UPRIGHT
    for x,y in zip(range(row-1,-1,-1), range(column+1,len(state),1)):
        if new_state[x][y] == ' ':
            break
        if new_state[x][y] != player:
            continue
        if new_state[x][y] == player:
            for cX,cY in zip(range(row-1, x, -1), range(column+1, y, 1)):
                new_state[cX][cY] = player
            break

    #FOR UPLEFT
    for x,y in zip(range(row-1,-1,-1), range(column-1,-1,-1)):
        if new_state[x][y] == ' ':
            break
        if new_state[x][y] != player:
            continue
        if new_state[x][y] == player:
            for cX,cY in zip(range(row-1, x, -1), range(column-1, y,-1)):
                new_state[cX][cY] = player
            break


    #FOR DOWNLEFT
    for x,y in zip(range(row+1,len(state),1), range(column-1,-1,-1)):
        if new_state[x][y] == ' ':
            break
        if new_state[x][y] != player:
            continue
        if new_state[x][y] == player:
            for cX,cY in zip(range(row+1, x, 1), range(column-1, y,-1)):
                new_state[cX][cY] = player
            break

    #FOR DOWNRIGHT
    for x,y in zip(range(row+1,len(state),1), range(column+1,len(state),1)):
        if new_state[x][y] == ' ':
            break
        if new_state[x][y] != player:
            continue
        if new_state[x][y] == player:
            for cX,cY in zip(range(row+1, x, 1), range(column+1, y, 1)):
                new_state[cX][cY] = player
            break

    return new_state


"""
A method for counting the pieces owned by the two players for a given state. The
return value should be two tuple in the format of (blackpeices, white pieces), e.g.,

    return (4, 3)

"""


def count_pieces(state):
    blackpieces = 0
    whitepieces = 0
    # Your implementation goes here
    for row in state:
        for i in row:
            if i == 'B':
                blackpieces = blackpieces + 1
            elif i == 'W':
                whitepieces = whitepieces + 1
    return (blackpieces, whitepieces)


"""
Check whether a state is a terminal state. 
"""


def is_terminal_state(state, state_list=None):
    terminal = False
    c= count_pieces(state)
    if (c[0] == 0 or c[1] == 0):
        return True
    # Your implementation goes here
    for i in range(len(state)):
        for j in range(len(state[i])):
            if state[i][j] == ' ':
                if get_move_value(state, 'B', i, j) != 0:
                    return terminal
                if get_move_value(state, 'W', i, j) != 0:
                    return terminal
    terminal = True
    return terminal


"""
The minimax algorithm. Your implementation should return the best value for the
given state and player, as well as the next immediate move to take for the player. 
"""


def minimax(state, player):
    value = 0
    row = -1
    column = -1
    # Your implementation goes here
    p = count_pieces(state)
    value = p[0] - p[1]
    if (is_terminal_state(state)):
        return (value, row, column)

    moves = []
    for x in range(0,len(state),1):
        for y in range(0, len(state),1):
            if (get_move_value(state,player,x,y) != 0):
                moves.append((x,y))

    #print player, moves
    if len(moves) == 0:
        return (value, row, column)

    if player == 'B':
        # finding max
        value = -9001
        for test in moves:
            (x, y) = test
            temp = minimax(execute_move(state, player, x, y), 'W')
            (v, r, c) = temp

            if v > value:
                value = v
                row = x
                column = y
    elif player == 'W':
        # Finding min
        value = 9001
        for test in moves:
            (x, y) = test
            temp = minimax(execute_move(state, player, x, y), 'B')
            (v, r, c) = temp

            if v < value:
                value = v
                row = x
                column = y
    return (value, row, column)


"""
This method should call the minimax algorithm to compute an optimal move sequence
that leads to an end game. 
"""


def full_minimax(state, player):
    value = 0
    move_sequence = []
    # Your implementation goes here
    r = 0
    c = 0
    p = player
    temp = state
    while is_terminal_state(state) is not True:
        (v, r, c) = minimax(state, p)

        if r == -1 and c == -1:
            if p == 'W':
                p = 'B'
            else:
                p = 'W'
            continue
        state = execute_move(state, p, r, c)
        value = v
        move_sequence.append((p, r, c))
        if p == 'B':
            p = 'W'
        else:
            p = 'B'
    move_sequence.append((p,-1,-1))
    return (value, move_sequence)



"""
The minimax algorithm with alpha-beta pruning. Your implementation should return the
best value for the given state and player, as well as the next immediate move to take
for the player. 
"""


def minimax_ab(state, player, alpha=-10000000, beta=10000000):
    value = 0
    row = -1
    column = -1
    # Your implementation goes here
    p = count_pieces(state)
    value = p[0] - p[1]
    if (is_terminal_state(state)):
        return (value,row,column)

    moves = []
    for x in range(0,len(state),1):
            for y in range(0, len(state),1):
                if (get_move_value(state,player,x,y) != 0):
                    moves.append((x,y))

    if len(moves) == 0:
        return (value, row, column)

    #for min
    if player == 'W':
        value = 9001
        for test in moves:
            (x, y) = test
            temp = minimax_ab(execute_move(state,player,x,y), 'B',alpha, beta)
            (v, r, c) = temp

            if v < value:
                value = v
                row = x
                column = y
            if v <= alpha:
                return (value,row,column)
            if v < beta:
                beta = v
    #For max
    if player == 'B':
        value = -9001
        for test in moves:
            (x, y) = test
            temp =  minimax_ab(execute_move(state,player,x,y), 'W',alpha, beta)
            (v, r, c) = temp

            if v > value:
                value = v
                row = x
                column = y
            if v >= beta:
                return (value,row,column)
            if v > alpha:
                alpha = v

    return (value, row, column)


"""
This method should call the minimax_ab algorithm to compute an optimal move sequence
that leads to an end game, using alpha-beta pruning.
"""


def full_minimax_ab(state, player):
    value = 0
    move_sequence = []
    # Your implementation goes here
    p = player
    temp = state

    while(not is_terminal_state(temp)):
        (v,r,c) = minimax_ab(temp,p)
        if r == -1 and c == -1:
            if p == 'W':
                p = 'B'
            else:
                p = 'W'
            continue
        temp = execute_move(temp,p,r,c)

        value = v
        move_sequence.append((p, r, c))

        if p == 'W':
            p = 'B'
        else:
            p = 'W'
    move_sequence.append((p,-1,-1))

    return (value, move_sequence)