def get_winning_positions(row_number, column_number) -> list:
    field = [[0] * column_number for i in range(row_number)]
    field[-1][-1] = '-'
    for row_index in range(row_number - 1, -1, -1):
        for column_index in range(column_number - 1, -1, -1):
            # check '-' in a rightward row
            if '-' in [column for i, column in enumerate(field[row_index]) if i > column_index]:
                field[row_index][column_index] = '+'
            # check '-' in a downward column
            elif '-' in [row[column_index] for i, row in enumerate(field) if i > row_index]:
                field[row_index][column_index] = '+'
            # check '-' in a diagonal
            # check the last row and the last column
            elif row_index < row_number - 1 and column_index < column_number - 1:
                diagonal = []
                column_ind = column_index
                for row in field[row_index + 1:]:
                    column_ind += 1
                    if column_ind > column_number - 1:
                        break
                    diagonal.append(row[column_ind])
                if '-' in diagonal:
                    field[row_index][column_index] = '+'
                else:
                    field[row_index][column_index] = '-'
    return field


if __name__ == '__main__':
    positions = get_winning_positions(6, 6)
    for row in positions:
        print(row)
        print()
