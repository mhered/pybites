IMPOSSIBLE = 'Mission impossible. No one can contribute.'


def max_fund(village):
    """Find a contiguous subarray with the largest sum."""
    # Hint: while iterating, you could save the best_sum collected so far
    # return total, starting, ending
    start = 0
    end = 0
    max_donations= float('-inf')
    for i in range(len(village)):
        for j in range(i+1,len(village)+1):
            donations = sum(village[i:j])
            # print(f"{i}:{j} ({village[i:j]})-> {donations}")
            if donations >= max_donations:
                max_donations = donations
                start = i
                end = j
                # print(f"Found max!")
    if max_donations < 0:
        print(IMPOSSIBLE)
        return (0,0,0)
    return (max_donations, start+1, end)
    

if __name__ == "__main__":
    print(max_fund([0, -3, 2, 1, -7, 5, 3, -1, 6]))
    print(max_fund([0, 1, -1, -5, 0, 4, -3, -2]))
    print(max_fund([0, 0, 0, 0, 1, -5, -2, -1, -3]))
    print(max_fund([-1, -2, -3, -4, -5]))

