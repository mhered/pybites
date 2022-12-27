from typing import List  # not needed when we upgrade to 3.9


def print_names_to_columns(names: List[str], cols: int = 2) -> None:
    formatted=['| '+'{0: <10}'.format(name) for name in names]

    n=len(names)
    rows=n//cols
    if rows:
        for i in range(rows):
            print("".join(formatted[i*cols:(i+1)*cols]))
    if n%cols:
        print("".join(formatted[rows*cols:n]))
    
    

names = 'Sara Tim Ana Julian Manolo Juan'.split()
print_names_to_columns(names,4)