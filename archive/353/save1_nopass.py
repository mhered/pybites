import typer  # use typer.run and typer.Argument


def sum_numbers(a: int, b: int):
    """Sums two numbers"""
    return a + b


def main(a: int, b:int):
    print(sum_numbers(a,b))

if __name__ == "__main__":
    typer.run(main)