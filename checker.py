"""
xxx...|||xxx...|||xxx...|||
864371259325849761971265843     436192587198657432257483916689734125713528694542916378

864 371 259     864325971
325 849 761     371849265
971 265 843     259761843

436 192 587     436198257
198 657 432     192657483
257 483 916     579432916

689 734 125     689713542
713 528 694     734528916
542 916 378     125694378
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
