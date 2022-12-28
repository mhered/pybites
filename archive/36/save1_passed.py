def get_profile(name: str, age: int, *sports, **awards):
    if not isinstance(age, int):
        raise ValueError
    if len(sports) > 5:
        raise ValueError
    result = {'name': name,
              'age': age
              }
    if sports:
        result['sports'] = sorted(list(sports))
    if awards:
        result['awards'] = awards
    return result


if __name__ == "__main__":
    print(get_profile('manolo', 47, 'ski', 'scuba diving', 'triathlon', participant='half ironman'))
    