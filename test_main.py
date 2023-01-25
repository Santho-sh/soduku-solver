from main import valid, empty_finder


board = [
    [7, 8, 0, 4, 0, 0, 1, 2, 0],
    [6, 0, 0, 0, 7, 5, 0, 0, 9],
    [0, 0, 0, 6, 0, 1, 0, 7, 8],
    [0, 0, 7, 0, 4, 0, 2, 6, 0],
    [0, 0, 1, 0, 5, 0, 9, 3, 0],
    [9, 0, 4, 0, 6, 0, 0, 0, 5],
    [0, 7, 0, 3, 0, 0, 0, 1, 2],
    [1, 2, 0, 0, 0, 7, 4, 0, 0],
    [0, 4, 9, 2, 0, 6, 0, 0, 7],
]


def test_valid():
    assert valid(board, 1, 0, 2) == False     
    assert valid(board, 2, 0, 2) == False     
    assert valid(board, 8, 0, 2) == False  
    
    assert valid(board, 3, 0, 2) == True     
    assert valid(board, 5, 0, 2) == True  
    
    
def test_empty_finder():

    assert empty_finder(board) == (0, 2)
       