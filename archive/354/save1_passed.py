import typer


def sum_numbers(a: int, b: int):
    return a + b


def main(
    a: int = typer.Argument(..., help="The value of the first summand"),
    b: int = typer.Argument(..., help="The value of the second summand"),
    c: int = typer.Option(None, help="The value to compare the sum."),
):
    """CLI that allows you to add two numbers"""

    if not c:
        COMPARISON = None
    elif c<sum_numbers(a, b):
        COMPARISON = "smaller" 
    elif c>=sum_numbers(a, b):
        COMPARISON = "not smaller"

    print(f"The sum is {sum_numbers(a, b)} and c is {COMPARISON}")


if __name__ == "__main__":
    typer.run(main)