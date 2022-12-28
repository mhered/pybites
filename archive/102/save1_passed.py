VALID_COLORS = ['blue', 'yellow', 'red']


def print_colors():
    """In the while loop ask the user to enter a color,
       lowercase it and store it in a variable. Next check: 
       - if 'quit' was entered for color, print 'bye' and break. 
       - if the color is not in VALID_COLORS, print 'Not a valid color' and continue.
       - otherwise print the color in lower case."""
    while True:
        try:
            user_input = input("Enter a color (blue/yellow/red) or quit to exit")
        except EOFError:
            break    
        user_input = user_input.lower()
        if user_input == "quit":
            print("bye")
            break
        if user_input not in VALID_COLORS:
            print("Not a valid color")
            continue
        print(user_input)


print_colors()
