import pytest

from workouts import print_workout_days

WORKOUTS = {'mon': 'upper body #1',
            'tue': 'lower body #1',
            'wed': '30 min cardio',
            'thu': 'upper body #2',
            'fri': 'lower body #2'}

@pytest.mark.parametrize("test_input, expected", [
    ("#1", 'Mon, Tue'), 
    ("body", 'Mon, Tue, Thu, Fri'), 
    ("cardio", 'Wed')
    ("other", 'No matching workout')
    ])
def test_print_workout_days(test_input, expected, capsys):
    print_workout_days(test_input)
    captured = capsys.readouterr()
    assert captured.out == expected
