import pytest
from typer.testing import CliRunner

from script import app


@pytest.fixture()
def runner() -> CliRunner:
    return CliRunner()


@pytest.mark.parametrize(
    "command, expected_result",
    [
        ("subtract 1 6", "The delta is -5"),
        ("subtract 8 5", "The delta is 3"),
    ],
)
def test_subtract(command:str, expected_result:str, runner:CliRunner):
    result = runner.invoke(app, command)
    assert result.exit_code == 0
    assert expected_result in result.stdout


@pytest.mark.parametrize(
    "command, expected_result",
    [
        ("compare 10 2", "d=2 is not greater than c=10"),
        ("compare 0 5", "d=5 is greater than c=0"),
        ("compare 3 3", "d=3 is not greater than c=3"),
    ],
)
def test_compare(command:str, expected_result:str, runner:CliRunner):
    result = runner.invoke(app, command)
    assert result.exit_code == 0
    assert expected_result in result.stdout

def test_help_msg(runner):
    result = runner.invoke(app, ["--help"])
    assert result.exit_code == 0
    assert "Command that allows you to add two numbers." in result.stdout
    assert "Command that checks whether a number d is greater than a number c." in result.stdout

def test_help_msg_subtract(runner):
    result = runner.invoke(app, ["subtract --help"])
    assert result.exit_code == 0    
    assert "The value of the first summand" in result.stdout
    assert "The value of the second summand" in result.stdout

def test_help_msg_compare(runner):
    result = runner.invoke(app, ["compare --help"])
    assert result.exit_code == 0    
    assert "First number to compare against." in result.stdout
    assert "Second number that is compared against first number." in result.stdout    
    

