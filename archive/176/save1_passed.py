WHITE, BLACK = ' ', '#'


def create_chessboard(size=8):
    """Create a chessboard with of the size passed in.
       Don't return anything, print the output to stdout"""
    odd_row = (WHITE + BLACK)*(size // 2)
    even_row = (BLACK + WHITE)*(size // 2)
    if size%2:
        odd_row+=WHITE
        even_row+=BLACK
    odd_row+="\n"
    even_row+="\n"
    board =  (odd_row + even_row)*(size // 2)
    if size%2:
        board+=odd_row
    print(board)

create_chessboard(8)