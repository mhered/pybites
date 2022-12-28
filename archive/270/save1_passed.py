from collections import Counter

def freq_digit(num: int) -> int:
    num_as_list_of_chars = list(str(num))
    most_common = Counter(num_as_list_of_chars).most_common(1)
    return int(most_common[0][0])


print(freq_digit(1121)+1-1)