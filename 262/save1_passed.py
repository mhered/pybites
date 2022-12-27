def calculate_gc_content(sequence):
    """
    Receives a DNA sequence (A, G, C, or T)
    Returns the percentage of GC content (rounded to the last two digits)
    """
    clean_sequence = "".join([letter for letter in sequence.upper() if letter in "AGCT"])
    total = len(clean_sequence)
    gc_count = len([letter for letter in clean_sequence if letter in "GC"])

    return round(100 * gc_count / total , 2)


percent = calculate_gc_content("a,G.c T\nAGcT")
print(f"{percent:0.2f}")
