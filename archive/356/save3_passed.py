import typer


def sum_numbers(a: int, b: int):
    return a + b


app = typer.Typer()
state = {"verbose": False} # MH


@app.command()
def sum(
    a: int = typer.Argument(..., help="The value of the first summand"),
    b: int = typer.Argument(..., help="The value of the second summand"),
):
    """Command that allows you to add two numbers."""
    sum_ab = sum_numbers(a, b)

    # MH: add an if-else to write verbose output as a function of the callback setting
    if state["verbose"]:
        print(f"The sum is {sum_ab}")
    else:
        print(f"{sum_ab}")


@app.command()
def compare(
    c: int = typer.Argument(..., help="First number to compare against."),
    d: int = typer.Argument(
        ..., help="Second number that is compared against first number."
    ),
):
    """Command that checks whether a number d is greater than a number c."""

    STRING_TRUE = "greater"
    STRING_FALSE = "not greater"

    d_greater_c = d > c

    c_evaluation = STRING_TRUE if d_greater_c else STRING_FALSE

    # MM: add an if-else to write verbose output as a function of the callback setting
    if state["verbose"]:
        print(f"{d=} is {c_evaluation} than {c=}")
    else:
        print(f"d > c: {d_greater_c}")


# MH: decorate this
@app.callback()
def main(
    verbose: bool = False
):
    """
    Have sum fun with numbers.
    """
    # MH: inform user and set state according to user input about verbosity
    if verbose:
        print("Will write verbose output")
        state["verbose"] = True



if __name__ == "__main__":
    app()