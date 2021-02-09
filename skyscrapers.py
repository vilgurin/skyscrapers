'''
This module contains functions
'''
import doctest
def read_input(path: str):

    """
    Read game board file from path.
    Return list of str.
    """
    
    input_lines = []

    with open(path, "r") as openfile:

        for line in openfile:
            line = line.strip("\n")
            input_lines.append(line)

    return input_lines


def left_to_right_check(input_line: str, pivot: int):

    """
    Check row-wise visibility from left to right.
    Return True if number of building from the left-most hint is visible looking to the right,
    False otherwise.

    input_line - representing board row.
    pivot - number on the left-most hint of the input_line.

    >>> left_to_right_check("412453*", 4)
    True
    >>> left_to_right_check("452453*", 5)
    False
    """

    input_line = input_line[:-1]
    max_difference = 0
    counter = 1
    max_difference = int(input_line[1]) - int(input_line[2])

    for i in range(1,len(input_line)):
        if int(input_line[i])-int(input_line[2])> max_difference:
            max_difference = int(input_line[i])-int(input_line[2])
            counter += 1 

    if counter == int(pivot):
        return True
        
    return False


def check_not_finished_board(board: list):

    """
    Check if skyscraper board is not finished, i.e., '?' present on the game board.

    Return True if finished, False otherwise.

    >>> check_not_finished_board(['***21**', '4?????*', '4?????*', '*?????5', '*?????*', '*?????*', '*2*1***'])
    False
    >>> check_not_finished_board(['***21**', '412453*', '423145*', '*543215', '*35214*', '*41532*', '*2*1***'])
    True
    >>> check_not_finished_board(['***21**', '412453*', '423145*', '*5?3215', '*35214*', '*41532*', '*2*1***'])
    False
    """

    for i in board:
        if "?" in i:
            return False

    return True


def check_uniqueness_in_rows(board: list):

    """
    Check buildings of unique height in each row.

    Return True if buildings in a row have unique length, False otherwise.

    >>> check_uniqueness_in_rows(['***21**', '412453*', '423145*', '*543215', '*35214*', '*41532*', '*2*1***'])
    True
    >>> check_uniqueness_in_rows(['***21**', '452453*', '423145*', '*543215', '*35214*', '*41532*', '*2*1***'])
    False
    >>> check_uniqueness_in_rows(['***21**', '412453*', '423145*', '*553215', '*35214*', '*41532*', '*2*1***'])
    False
    """

    for i in board[1:-1]:
        i = i[1:-1]

        for j in range(len(i)):
            if i[j] != "*":
                counter = i.count(str(i[j]))
                if counter > 1:
                    return False
        counter = 0

    return True


def check_horizontal_visibility(board: list):

    """
    Check row-wise visibility (left-right and vice versa)

    Return True if all horizontal hints are satisfiable,
     i.e., for line 412453* , hint is 4, and 1245 are the four buildings
      that could be observed from the hint looking to the right.

    >>> check_horizontal_visibility(['***21**', '412453*', '423145*', '*543215', '*35214*', '*41532*', '*2*1***'])
    True
    >>> check_horizontal_visibility(['***21**', '452453*', '423145*', '*543215', '*35214*', '*41532*', '*2*1***'])
    False
    >>> check_horizontal_visibility(['***21**', '452413*', '423145*', '*543215', '*35214*', '*41532*', '*2*1***'])
    False
    """

    for i in board:

        if i[0].isdigit() == True:
            check_rows = (left_to_right_check(i, i[0]))

            if check_rows == False:
                return False

        elif i[-1].isdigit() == True:
            check_rows = (left_to_right_check(i[::-1], i[-1]))

            if check_rows == False:
                return False

    return True



def check_columns(board: list):

    """
    Check column-wise compliance of the board for uniqueness (buildings of unique height)
    and visibility (top-bottom and vice versa).
    Same as for horizontal cases, but aggregated in one function for vertical case, i.e. columns.

    >>> check_columns(['***21**', '412453*', '423145*', '*543215', '*35214*', '*41532*', '*2*1***'])
    True
    >>> check_columns(['***21**', '412453*', '423145*', '*543215', '*35214*', '*41232*', '*2*1***'])
    False
    >>> check_columns(['***21**', '412553*', '423145*', '*543215', '*35214*', '*41532*', '*2*1***'])
    False
    """

    vertical_list = []
    for i in range(len(board[0])):
        if board[0][i].isdigit() == True:
            for elem in board:
                vertical_list.append(elem[i])
            vertical_list = "".join(vertical_list)
            for i in vertical_list[1:-1]:
                if vertical_list[1:-1].count(i) > 1:
                    return False
            if left_to_right_check(vertical_list,vertical_list[0]) == False:
                return False
            vertical_list = []


    for i in range(len(board[-1])):
        if board[-1][i].isdigit() == True:

            for elem in board[1:]:
                vertical_list.append(elem[i])
            vertical_list = "".join(vertical_list)
            vertical_list = vertical_list[::-1]

            for i in vertical_list[1:-1]:
                if vertical_list[1:-1].count(i) > 1:
                    return False

            if left_to_right_check(vertical_list,vertical_list[0]) == False:
                return False

            vertical_list = []

    return True


def check_skyscrapers(input_path: str):

    """
    Main function to check the status of skyscraper game board.
    Return True if the board status is compliant with the rules,
    False otherwise.
    """

    board = read_input(input_path)

    check_horizontal = check_horizontal_visibility(board)
    check_column = check_columns(board)
    check_finished_board = check_not_finished_board(board)

    if (check_horizontal == True) and (check_column == True) \
            and (check_finished_board == True):

        return True

    return False
