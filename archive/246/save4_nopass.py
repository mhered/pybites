import pytest

from workouts import print_workout_days

@pytest.mark.parametrize("test_input, expected", [
        ("#1", 'Mon, Tue\n'), 
        ("body", 'Mon, Tue, Thu, Fri\n\n'), 
        ("cardio", 'Wed\n'),
        ("other", 'No matching workout\n')
    ])
def test_print_workout_days(test_input, expected, capsys):
    print_workout_days(test_input)
    captured = capsys.readouterr()
    assert captured.out == expected
