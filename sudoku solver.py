
def sudoku_solver(sudoku):
    """
    Solves a Sudoku puzzle and returns its unique solution.

    Input
        sudoku : 9x9 numpy array
            Empty cells are designated by 0.

    Output
        9x9 numpy array of integers
            It contains the solution, if there is one. If there is no solution, all array entries should be -1.
    """
    import numpy as np
    valid_state = True 
    rows_check = []
    columns_check = []
    for x in range(1,10) : 
        rows = np.count_nonzero(sudoku == x, axis = 1)
        columns = np.count_nonzero(sudoku == x, axis = 0)
        for y in rows : 
            rows_check.append(y)
        for z in columns : 
            columns_check.append(z)
    for a in set(rows_check) : 
        if a > 1 : 
            valid_state = False
            for x,y in np.ndenumerate(sudoku) : 
                sudoku[x[0]][x[1]] = -1
    for b in set(columns_check) : 
        if b > 1 : 
            valid_state = False 
            for x,y in np.ndenumerate(sudoku) : 
                sudoku[x[0]][x[1]] = -1
    while np.sum(sudoku) != 405 and valid_state :
        not_in_row_1 = [x for x in range(1,10) if x not in sudoku[0,:]]
        not_in_row_2 = [x for x in range(1,10) if x not in sudoku[1,:]]
        not_in_row_3 = [x for x in range(1,10) if x not in sudoku[2,:]]
        not_in_row_4 = [x for x in range(1,10) if x not in sudoku[3,:]]
        not_in_row_5 = [x for x in range(1,10) if x not in sudoku[4,:]]
        not_in_row_6 = [x for x in range(1,10) if x not in sudoku[5,:]]
        not_in_row_7 = [x for x in range(1,10) if x not in sudoku[6,:]]
        not_in_row_8 = [x for x in range(1,10) if x not in sudoku[7,:]]
        not_in_row_9 = [x for x in range(1,10) if x not in sudoku[8,:]]
        not_in_column_1 = [x for x in range(1,10) if x not in sudoku[:,0]]
        not_in_column_2 = [x for x in range(1,10) if x not in sudoku[:,1]]
        not_in_column_3 = [x for x in range(1,10) if x not in sudoku[:,2]]
        not_in_column_4 = [x for x in range(1,10) if x not in sudoku[:,3]]
        not_in_column_5 = [x for x in range(1,10) if x not in sudoku[:,4]]
        not_in_column_6 = [x for x in range(1,10) if x not in sudoku[:,5]]
        not_in_column_7 = [x for x in range(1,10) if x not in sudoku[:,6]]
        not_in_column_8 = [x for x in range(1,10) if x not in sudoku[:,7]]
        not_in_column_9 = [x for x in range(1,10) if x not in sudoku[:,8]]
        not_in_subblock_1 = [x for x in range(1,10) if x not in sudoku[0:3,0:3]]
        not_in_subblock_2 = [x for x in range(1,10) if x not in sudoku[0:3,3:6]]
        not_in_subblock_3 = [x for x in range(1,10) if x not in sudoku[0:3,6:]]
        not_in_subblock_4 = [x for x in range(1,10) if x not in sudoku[3:6,0:3]]
        not_in_subblock_5 = [x for x in range(1,10) if x not in sudoku[3:6,3:6]]
        not_in_subblock_6 = [x for x in range(1,10) if x not in sudoku[3:6,6:]]
        not_in_subblock_7 = [x for x in range(1,10) if x not in sudoku[6:,0:3]]
        not_in_subblock_8 = [x for x in range(1,10) if x not in sudoku[6:,3:6]]
        not_in_subblock_9 = [x for x in range(1,10) if x not in sudoku[6:,6:]]
        all_indices = []
        for idx, x in np.ndenumerate(sudoku) : 
            all_indices.append(idx)
        subblock_1_indices = [x for x in all_indices if x[0] in [0,1,2] and x[1] in [0,1,2]]
        subblock_2_indices = [x for x in all_indices if x[0] in [0,1,2] and x[1] in [3,4,5]]
        subblock_3_indices = [x for x in all_indices if x[0] in [0,1,2] and x[1] in [6,7,8]]
        subblock_4_indices = [x for x in all_indices if x[0] in [3,4,5] and x[1] in [0,1,2]]
        subblock_5_indices = [x for x in all_indices if x[0] in [3,4,5] and x[1] in [3,4,5]]
        subblock_6_indices = [x for x in all_indices if x[0] in [3,4,5] and x[1] in [6,7,8]]
        subblock_7_indices = [x for x in all_indices if x[0] in [6,7,8] and x[1] in [0,1,2]]
        subblock_8_indices = [x for x in all_indices if x[0] in [6,7,8] and x[1] in [3,4,5]]
        subblock_9_indices = [x for x in all_indices if x[0] in [6,7,8] and x[1] in [6,7,8]]
        empty_fields = []
        for idx, x in np.ndenumerate(sudoku):
            if x == 0 : 
                empty_fields.append(idx)
        not_in_all_columns = [not_in_column_1, not_in_column_2, not_in_column_3, not_in_column_4, not_in_column_5, 
                              not_in_column_6, not_in_column_7, not_in_column_8, not_in_column_9]
        not_in_all_rows = [not_in_row_1, not_in_row_2,not_in_row_3,not_in_row_4,not_in_row_5,
                           not_in_row_6,not_in_row_7,not_in_row_8,not_in_row_9]
        not_in_all_subblocks = [not_in_subblock_1,not_in_subblock_2,not_in_subblock_3,not_in_subblock_4,not_in_subblock_5,not_in_subblock_6,
                                not_in_subblock_7,not_in_subblock_8,not_in_subblock_9]
        possible_solutions_sequence = dict()
        for x in empty_fields : 
            if x in subblock_1_indices : 
                row_num = x[0]
                col_num = x[1]
                tmp = [number for number in range(1,10) if number in not_in_subblock_1 and number in not_in_all_rows[row_num] 
                       and number in not_in_all_columns[col_num]]
                possible_solutions_sequence[x] = tmp 
            elif x in subblock_2_indices : 
                row_num = x[0]
                col_num = x[1]
                tmp = [number for number in range(1,10) if number in not_in_subblock_2 and number in not_in_all_rows[row_num] 
                       and number in not_in_all_columns[col_num]]
                possible_solutions_sequence[x] = tmp
            elif x in subblock_3_indices : 
                row_num = x[0]
                col_num = x[1]
                tmp = [number for number in range(1,10) if number in not_in_subblock_3 and number in not_in_all_rows[row_num] 
                       and number in not_in_all_columns[col_num]]
                possible_solutions_sequence[x] = tmp
            elif x in subblock_4_indices : 
                row_num = x[0]
                col_num = x[1]
                tmp = [number for number in range(1,10) if number in not_in_subblock_4 and number in not_in_all_rows[row_num] 
                       and number in not_in_all_columns[col_num]]
                possible_solutions_sequence[x] = tmp
            elif x in subblock_5_indices : 
                row_num = x[0]
                col_num = x[1]
                tmp = [number for number in range(1,10) if number in not_in_subblock_5 and number in not_in_all_rows[row_num] 
                       and number in not_in_all_columns[col_num]]
                possible_solutions_sequence[x] = tmp
            elif x in subblock_6_indices : 
                row_num = x[0]
                col_num = x[1]
                tmp = [number for number in range(1,10) if number in not_in_subblock_6 and number in not_in_all_rows[row_num] 
                       and number in not_in_all_columns[col_num]]
                possible_solutions_sequence[x] = tmp
            elif x in subblock_7_indices : 
                row_num = x[0]
                col_num = x[1]
                tmp = [number for number in range(1,10) if number in not_in_subblock_7 and number in not_in_all_rows[row_num] 
                       and number in not_in_all_columns[col_num]]
                possible_solutions_sequence[x] = tmp
            elif x in subblock_8_indices : 
                row_num = x[0]
                col_num = x[1]
                tmp = [number for number in range(1,10) if number in not_in_subblock_8 and number in not_in_all_rows[row_num] 
                       and number in not_in_all_columns[col_num]]
                possible_solutions_sequence[x] = tmp
            elif x in subblock_9_indices : 
                row_num = x[0]
                col_num = x[1]
                tmp = [number for number in range(1,10) if number in not_in_subblock_9 and number in not_in_all_rows[row_num] 
                       and number in not_in_all_columns[col_num]]
                possible_solutions_sequence[x] = tmp
        fields_single_solutions = [x for x in [y for y in possible_solutions_sequence.values()] if len(x) == 1]
        if len(fields_single_solutions) > 0 : 
            for x in empty_fields : 
                if len(possible_solutions_sequence[x]) == 1 :
                    sudoku[x[0], x[1]] = possible_solutions_sequence[x][0]
        else : 
            subblock_1_hash = {}
            subblock_2_hash = {}
            subblock_3_hash = {}
            subblock_4_hash = {}
            subblock_5_hash = {}
            subblock_6_hash = {}
            subblock_7_hash = {}
            subblock_8_hash = {}
            subblock_9_hash = {}
            for x in empty_fields : 
                if len(possible_solutions_sequence[x]) > 1 and x in subblock_1_indices : 
                    subblock_1_hash[x] = possible_solutions_sequence[x]
                elif len(possible_solutions_sequence[x]) > 1 and x in subblock_2_indices : 
                    subblock_2_hash[x] = possible_solutions_sequence[x]
                elif len(possible_solutions_sequence[x]) > 1 and x in subblock_3_indices : 
                    subblock_3_hash[x] = possible_solutions_sequence[x]
                elif len(possible_solutions_sequence[x]) > 1 and x in subblock_4_indices : 
                    subblock_4_hash[x] = possible_solutions_sequence[x]
                elif len(possible_solutions_sequence[x]) > 1 and x in subblock_5_indices : 
                    subblock_5_hash[x] = possible_solutions_sequence[x]
                elif len(possible_solutions_sequence[x]) > 1 and x in subblock_6_indices : 
                    subblock_6_hash[x] = possible_solutions_sequence[x]
                elif len(possible_solutions_sequence[x]) > 1 and x in subblock_7_indices : 
                    subblock_7_hash[x] = possible_solutions_sequence[x]
                elif len(possible_solutions_sequence[x]) > 1 and x in subblock_8_indices : 
                    subblock_8_hash[x] = possible_solutions_sequence[x]
                elif len(possible_solutions_sequence[x]) > 1 and x in subblock_9_indices : 
                    subblock_9_hash[x] = possible_solutions_sequence[x]     
            solutions_block_1 = [val for sublist in [x for x in subblock_1_hash.values()] for val in sublist]
            solutions_block_2 = [val for sublist in [x for x in subblock_2_hash.values()] for val in sublist]
            solutions_block_3 = [val for sublist in [x for x in subblock_3_hash.values()] for val in sublist]
            solutions_block_4 = [val for sublist in [x for x in subblock_4_hash.values()] for val in sublist]
            solutions_block_5 = [val for sublist in [x for x in subblock_5_hash.values()] for val in sublist]
            solutions_block_6 = [val for sublist in [x for x in subblock_6_hash.values()] for val in sublist]
            solutions_block_7 = [val for sublist in [x for x in subblock_7_hash.values()] for val in sublist]
            solutions_block_8 = [val for sublist in [x for x in subblock_8_hash.values()] for val in sublist]
            solutions_block_9 = [val for sublist in [x for x in subblock_9_hash.values()] for val in sublist]
            unique_solutions_block_1 = [x for x in solutions_block_1 if solutions_block_1.count(x) == 1]
            unique_solutions_block_2 = [x for x in solutions_block_2 if solutions_block_2.count(x) == 1]
            unique_solutions_block_3 = [x for x in solutions_block_3 if solutions_block_3.count(x) == 1]
            unique_solutions_block_4 = [x for x in solutions_block_4 if solutions_block_4.count(x) == 1]
            unique_solutions_block_5 = [x for x in solutions_block_5 if solutions_block_5.count(x) == 1]
            unique_solutions_block_6 = [x for x in solutions_block_6 if solutions_block_6.count(x) == 1]
            unique_solutions_block_7 = [x for x in solutions_block_7 if solutions_block_7.count(x) == 1]
            unique_solutions_block_8 = [x for x in solutions_block_8 if solutions_block_8.count(x) == 1]
            unique_solutions_block_9 = [x for x in solutions_block_9 if solutions_block_9.count(x) == 1]
            for x, y in enumerate(empty_fields) :
                if y in subblock_1_indices : 
                    for x in subblock_1_hash.items() : 
                        for y in unique_solutions_block_1 : 
                            if y in x[1] : 
                                sudoku[x[0][0], x[0][1]] = y
                elif y in subblock_2_indices : 
                    for x in subblock_2_hash.items() : 
                        for y in unique_solutions_block_2 : 
                            if y in x[1] : 
                                sudoku[x[0][0], x[0][1]] = y
                elif y in subblock_3_indices : 
                    for x in subblock_3_hash.items() : 
                        for y in unique_solutions_block_3 : 
                            if y in x[1] : 
                                sudoku[x[0][0], x[0][1]] = y
                elif y in subblock_4_indices : 
                    for x in subblock_4_hash.items() : 
                        for y in unique_solutions_block_4 : 
                            if y in x[1] : 
                                sudoku[x[0][0], x[0][1]] = y
                elif y in subblock_5_indices : 
                    for x in subblock_5_hash.items() : 
                        for y in unique_solutions_block_5 : 
                            if y in x[1] : 
                                sudoku[x[0][0], x[0][1]] = y
                elif y in subblock_6_indices : 
                    for x in subblock_6_hash.items() : 
                        for y in unique_solutions_block_6 : 
                            if y in x[1] : 
                                sudoku[x[0][0], x[0][1]] = y
                elif y in subblock_7_indices : 
                    for x in subblock_7_hash.items() : 
                        for y in unique_solutions_block_7 : 
                            if y in x[1] : 
                                sudoku[x[0][0], x[0][1]] = y
                elif y in subblock_8_indices : 
                    for x in subblock_8_hash.items() : 
                        for y in unique_solutions_block_8 : 
                            if y in x[1] : 
                                sudoku[x[0][0], x[0][1]] = y
                elif y in subblock_9_indices : 
                    for x in subblock_9_hash.items() : 
                        for y in unique_solutions_block_9 : 
                            if y in x[1] : 
                                sudoku[x[0][0], x[0][1]] = y
            row_1_hash = {}
            row_2_hash = {}
            row_3_hash = {}
            row_4_hash = {}
            row_5_hash = {}
            row_6_hash = {}
            row_7_hash = {}
            row_8_hash = {}
            row_9_hash = {}
            row_1_indices = [x for x in all_indices if x[0] == 0]
            row_2_indices = [x for x in all_indices if x[0] == 1]
            row_3_indices = [x for x in all_indices if x[0] == 2]
            row_4_indices = [x for x in all_indices if x[0] == 3]
            row_5_indices = [x for x in all_indices if x[0] == 4]
            row_6_indices = [x for x in all_indices if x[0] == 5]
            row_7_indices = [x for x in all_indices if x[0] == 6]
            row_8_indices = [x for x in all_indices if x[0] == 7]
            row_9_indices = [x for x in all_indices if x[0] == 8]
            for x in empty_fields : 
                if len(possible_solutions_sequence[x]) > 1 and x in row_1_indices : 
                    row_1_hash[x] = possible_solutions_sequence[x]
                elif len(possible_solutions_sequence[x]) > 1 and x in row_2_indices : 
                    row_2_hash[x] = possible_solutions_sequence[x]
                elif len(possible_solutions_sequence[x]) > 1 and x in row_3_indices : 
                    row_3_hash[x] = possible_solutions_sequence[x]
                elif len(possible_solutions_sequence[x]) > 1 and x in row_4_indices : 
                    row_4_hash[x] = possible_solutions_sequence[x]
                elif len(possible_solutions_sequence[x]) > 1 and x in row_5_indices : 
                    row_5_hash[x] = possible_solutions_sequence[x]
                elif len(possible_solutions_sequence[x]) > 1 and x in row_6_indices : 
                    row_6_hash[x] = possible_solutions_sequence[x]
                elif len(possible_solutions_sequence[x]) > 1 and x in row_7_indices : 
                    row_7_hash[x] = possible_solutions_sequence[x]
                elif len(possible_solutions_sequence[x]) > 1 and x in row_8_indices : 
                    row_8_hash[x] = possible_solutions_sequence[x]
                elif len(possible_solutions_sequence[x]) > 1 and x in row_9_indices : 
                    row_9_hash[x] = possible_solutions_sequence[x] 
            solutions_row_1 = [val for sublist in [x for x in row_1_hash.values()] for val in sublist]
            solutions_row_2 = [val for sublist in [x for x in row_2_hash.values()] for val in sublist]
            solutions_row_3 = [val for sublist in [x for x in row_3_hash.values()] for val in sublist]
            solutions_row_4 = [val for sublist in [x for x in row_4_hash.values()] for val in sublist]
            solutions_row_5 = [val for sublist in [x for x in row_5_hash.values()] for val in sublist]
            solutions_row_6 = [val for sublist in [x for x in row_6_hash.values()] for val in sublist]
            solutions_row_7 = [val for sublist in [x for x in row_7_hash.values()] for val in sublist]
            solutions_row_8 = [val for sublist in [x for x in row_8_hash.values()] for val in sublist]
            solutions_row_9 = [val for sublist in [x for x in row_9_hash.values()] for val in sublist]
            unique_solutions_row_1 = [x for x in solutions_row_1 if solutions_row_1.count(x) == 1]
            unique_solutions_row_2 = [x for x in solutions_row_2 if solutions_row_2.count(x) == 1]
            unique_solutions_row_3 = [x for x in solutions_row_3 if solutions_row_3.count(x) == 1]
            unique_solutions_row_4 = [x for x in solutions_row_4 if solutions_row_4.count(x) == 1]
            unique_solutions_row_5 = [x for x in solutions_row_5 if solutions_row_5.count(x) == 1]
            unique_solutions_row_6 = [x for x in solutions_row_6 if solutions_row_6.count(x) == 1]
            unique_solutions_row_7 = [x for x in solutions_row_7 if solutions_row_7.count(x) == 1]
            unique_solutions_row_8 = [x for x in solutions_row_8 if solutions_row_8.count(x) == 1]
            unique_solutions_row_9 = [x for x in solutions_row_9 if solutions_row_9.count(x) == 1]
            for x, y in enumerate(empty_fields) :
                if y in row_1_indices : 
                    for x in row_1_hash.items() : 
                        for y in unique_solutions_row_1 : 
                            if y in x[1] : 
                                sudoku[x[0][0], x[0][1]] = y
                elif y in row_2_indices : 
                    for x in row_2_hash.items() : 
                        for y in unique_solutions_row_2 : 
                            if y in x[1] : 
                                sudoku[x[0][0], x[0][1]] = y
                elif y in row_3_indices : 
                    for x in row_3_hash.items() : 
                        for y in unique_solutions_row_3 : 
                            if y in x[1] : 
                                sudoku[x[0][0], x[0][1]] = y
                elif y in row_3_indices : 
                    for x in row_3_hash.items() : 
                        for y in unique_solutions_row_3 : 
                            if y in x[1] : 
                                sudoku[x[0][0], x[0][1]] = y
                elif y in row_4_indices : 
                    for x in row_4_hash.items() : 
                        for y in unique_solutions_row_4 : 
                            if y in x[1] : 
                                sudoku[x[0][0], x[0][1]] = y
                elif y in row_5_indices : 
                    for x in row_5_hash.items() : 
                        for y in unique_solutions_row_5 : 
                            if y in x[1] : 
                                sudoku[x[0][0], x[0][1]] = y
                elif y in row_6_indices : 
                    for x in row_6_hash.items() : 
                        for y in unique_solutions_row_6 : 
                            if y in x[1] : 
                                sudoku[x[0][0], x[0][1]] = y
                elif y in row_7_indices : 
                    for x in row_7_hash.items() : 
                        for y in unique_solutions_row_7 : 
                            if y in x[1] : 
                                sudoku[x[0][0], x[0][1]] = y
                elif y in row_8_indices : 
                    for x in row_8_hash.items() : 
                        for y in unique_solutions_row_8 : 
                            if y in x[1] : 
                                sudoku[x[0][0], x[0][1]] = y
                elif y in row_9_indices : 
                    for x in row_9_hash.items() : 
                        for y in unique_solutions_row_9 : 
                            if y in x[1] : 
                                sudoku[x[0][0], x[0][1]] = y
            column_1_hash = {}
            column_2_hash = {}
            column_3_hash = {}
            column_4_hash = {}
            column_5_hash = {}
            column_6_hash = {}
            column_7_hash = {}
            column_8_hash = {}
            column_9_hash = {}
            column_1_indices = [x for x in all_indices if x[1] == 0]
            column_2_indices = [x for x in all_indices if x[1] == 1]
            column_3_indices = [x for x in all_indices if x[1] == 2]
            column_4_indices = [x for x in all_indices if x[1] == 3]
            column_5_indices = [x for x in all_indices if x[1] == 4]
            column_6_indices = [x for x in all_indices if x[1] == 5]
            column_7_indices = [x for x in all_indices if x[1] == 6]
            column_8_indices = [x for x in all_indices if x[1] == 7]
            column_9_indices = [x for x in all_indices if x[1] == 8]
            for x in empty_fields : 
                if len(possible_solutions_sequence[x]) > 1 and x in column_1_indices : 
                    column_1_hash[x] = possible_solutions_sequence[x]
                elif len(possible_solutions_sequence[x]) > 1 and x in column_2_indices : 
                    column_2_hash[x] = possible_solutions_sequence[x]
                elif len(possible_solutions_sequence[x]) > 1 and x in column_3_indices : 
                    column_3_hash[x] = possible_solutions_sequence[x]
                elif len(possible_solutions_sequence[x]) > 1 and x in column_4_indices : 
                    column_4_hash[x] = possible_solutions_sequence[x]
                elif len(possible_solutions_sequence[x]) > 1 and x in column_5_indices : 
                    column_5_hash[x] = possible_solutions_sequence[x]
                elif len(possible_solutions_sequence[x]) > 1 and x in column_6_indices : 
                    column_6_hash[x] = possible_solutions_sequence[x]
                elif len(possible_solutions_sequence[x]) > 1 and x in column_7_indices : 
                    column_7_hash[x] = possible_solutions_sequence[x]
                elif len(possible_solutions_sequence[x]) > 1 and x in column_8_indices : 
                    column_8_hash[x] = possible_solutions_sequence[x]
                elif len(possible_solutions_sequence[x]) > 1 and x in column_9_indices : 
                    column_9_hash[x] = possible_solutions_sequence[x] 
            solutions_column_1 = [val for sublist in [x for x in column_1_hash.values()] for val in sublist]
            solutions_column_2 = [val for sublist in [x for x in column_2_hash.values()] for val in sublist]
            solutions_column_3 = [val for sublist in [x for x in column_3_hash.values()] for val in sublist]
            solutions_column_4 = [val for sublist in [x for x in column_4_hash.values()] for val in sublist]
            solutions_column_5 = [val for sublist in [x for x in column_5_hash.values()] for val in sublist]
            solutions_column_6 = [val for sublist in [x for x in column_6_hash.values()] for val in sublist]
            solutions_column_7 = [val for sublist in [x for x in column_7_hash.values()] for val in sublist]
            solutions_column_8 = [val for sublist in [x for x in column_8_hash.values()] for val in sublist]
            solutions_column_9 = [val for sublist in [x for x in column_9_hash.values()] for val in sublist]
            unique_solutions_column_1 = [x for x in solutions_column_1 if solutions_column_1.count(x) == 1]
            unique_solutions_column_2 = [x for x in solutions_column_2 if solutions_column_2.count(x) == 1]
            unique_solutions_column_3 = [x for x in solutions_column_3 if solutions_column_3.count(x) == 1]
            unique_solutions_column_4 = [x for x in solutions_column_4 if solutions_column_4.count(x) == 1]
            unique_solutions_column_5 = [x for x in solutions_column_5 if solutions_column_5.count(x) == 1]
            unique_solutions_column_6 = [x for x in solutions_column_6 if solutions_column_6.count(x) == 1]
            unique_solutions_column_7 = [x for x in solutions_column_7 if solutions_column_7.count(x) == 1]
            unique_solutions_column_8 = [x for x in solutions_column_8 if solutions_column_8.count(x) == 1]
            unique_solutions_column_9 = [x for x in solutions_column_9 if solutions_column_9.count(x) == 1]
            for x, y in enumerate(empty_fields) :
                if y in column_1_indices : 
                    for x in column_1_hash.items() : 
                        for y in unique_solutions_column_1 : 
                            if y in x[1] : 
                                sudoku[x[0][0], x[0][1]] = y
                elif y in column_2_indices : 
                    for x in column_2_hash.items() : 
                        for y in unique_solutions_column_2 : 
                            if y in x[1] : 
                                sudoku[x[0][0], x[0][1]] = y
                elif y in column_3_indices : 
                    for x in column_3_hash.items() : 
                        for y in unique_solutions_column_3 : 
                            if y in x[1] : 
                                sudoku[x[0][0], x[0][1]] = y
                elif y in column_3_indices : 
                    for x in column_3_hash.items() : 
                        for y in unique_solutions_column_3 : 
                            if y in x[1] : 
                                sudoku[x[0][0], x[0][1]] = y
                elif y in column_4_indices : 
                    for x in column_4_hash.items() : 
                        for y in unique_solutions_column_4 : 
                            if y in x[1] : 
                                sudoku[x[0][0], x[0][1]] = y
                elif y in column_5_indices : 
                    for x in column_5_hash.items() : 
                        for y in unique_solutions_column_5 : 
                            if y in x[1] : 
                                sudoku[x[0][0], x[0][1]] = y
                elif y in column_6_indices : 
                    for x in column_6_hash.items() : 
                        for y in unique_solutions_column_6 : 
                            if y in x[1] : 
                                sudoku[x[0][0], x[0][1]] = y
                elif y in column_7_indices : 
                    for x in column_7_hash.items() : 
                        for y in unique_solutions_column_7 : 
                            if y in x[1] : 
                                sudoku[x[0][0], x[0][1]] = y
                elif y in column_8_indices : 
                    for x in column_8_hash.items() : 
                        for y in unique_solutions_column_8 : 
                            if y in x[1] : 
                                sudoku[x[0][0], x[0][1]] = y
                elif y in column_9_indices : 
                    for x in column_9_hash.items() : 
                        for y in unique_solutions_column_9 : 
                            if y in x[1] : 
                                sudoku[x[0][0], x[0][1]] = y
    return sudoku