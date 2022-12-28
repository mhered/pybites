from itertools import cycle
import sys
from time import time, sleep

SPINNER_STATES = ['-', '\\', '|', '/']  # had to escape \
STATE_TRANSITION_TIME = 0.1


def spinner(seconds):
    """Make a terminal loader/spinner animation using the imports above.
       Takes seconds argument = time for the spinner to run.
       Does not return anything, only prints to stdout."""

    print(" ", end='', flush=True)
    # Back up one character then print our next frame in the animation
    for i, frame in enumerate(cycle(SPINNER_STATES)):
        print('\b', frame, sep='', end='', flush=True)
        sleep(STATE_TRANSITION_TIME)
        if i > seconds/STATE_TRANSITION_TIME:
            break
    print('\b ')


if __name__ == '__main__':
    spinner(2)
