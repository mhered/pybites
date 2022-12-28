import pytest
from typer.testing import CliRunner

from script import app


@pytest.fixture()
def runner() -> CliRunner:
    return CliRunner()
    
    
runner = CliRunner()


def test_app(runner):
    result = runner.invoke(app, ["Manolo"])
    assert result.exit_code == 0
    assert "Hello Manolo!" in result.stdout


def test_help_msg(runner):
    result = runner.invoke(app, ["--help"])
    assert result.exit_code == 0
    assert "CLI that allows you to greet a person." in result.stdout
    assert "The name of the person to greet." in result.stdout
