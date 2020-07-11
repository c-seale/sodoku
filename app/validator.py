"""
004300209
005009001
070060043
006002087
190007400
050083000
600000105
003508690
042910300

864371259
325849761
971265843
436192587
198657432
257483916
689734125
713528694
542916378
"""


def check_solution(board_state: str) -> bool:
    """
    Check to see if a sudoku board state string is a valid solution
    :param board_state: string describing a sudoku board state
    :return:
    """
    rows = list()
    columns = list()

    # Some quick sanity checks
    if len(board_state) != 81:
        return False
    if '0' in board_state:
        return False
    if sum(int(d) for d in board_state) != 405:  # verify overall solution sum
        return False
    for row in [board_state[i:i + 9] for i in range(0, len(board_state), 9)]:  # verify sums for every row
        rows.append(row)
        if sum(int(d) for d in row) != 45:
            return False
    for col in [board_state[i::9] for i in range(0, 9)]:  # verify sums for every column
        columns.append(col)
        if sum(int(d) for d in col) != 45:
            return False
    for row in rows:  # verify no duplicates in rows
        check = set()
        for val in row:
            check.add(val)
        if len(row) != len(check):
            return False
    for col in columns:  # verify no duplicates in columns
        check = set()
        for val in col:
            check.add(val)
        if len(col) != len(check):
            return False
    # TODO: Verify sums in each 3x3 block
    # TODO: Check for duplicates in each 3x3 block
    return True
