def countdown_for(start=10):
    for i in reversed(range(1, start + 1)):
        print(i)
    print('time is up')


def countdown_recursive(start=10):
    print(start)
    if start == 1:
        print('time is up')
        return             # Terminate recursion
    else:
        countdown_recursive(start - 1)   # Recursive call


countdown_recursive(10)
