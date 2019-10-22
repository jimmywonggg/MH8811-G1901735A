def TicTacDraw(board):
    # init line index
    line_index = 1
    for line in board:
        #init column index and line str
        column_index = 0
        line_str = ''
        # print line str
        for i in line:
            if i == 0:
                symbol = 'O'
            elif i == 1:
                symbol = 'X'
            elif i == 2:
                symbol = ' '
            # if column index larger than 0, line str add '|'
            if column_index > 0:
                line_str += '|'
            # line str add symbol
            line_str += ' ' + symbol + ' '
            column_index += 1
        print(line_str)
        # if line index less than line length, print split line
        if line_index < len(line):
            split_line = '-' * (4 * len(line) - 1)
            print(split_line)
        line_index += 1
        

board = [[0, 1, 2], [2, 0, 1], [1, 0, 2]]
TicTacDraw(board)