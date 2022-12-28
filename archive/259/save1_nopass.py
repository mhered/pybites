# See tests for a more comprehensive complementary table
SIMPLE_COMPLEMENTS_STR = """#Reduced table with bases A, G, C, T
 Base	Complementary Base
 A	T
 T	A
 G	C
 C	G
"""


def _read_str_table(str_table):
    """
    Takes a string defining a table of valid and comlementary bases 
    and returns a dict of base:complement
    """
    lst = [line.split() for line in str_table.splitlines()[2:]]
    return  {item[0].upper().strip(): item[-1].upper().strip() for item in lst}

# Recommended helper function
def _clean_sequence(sequence, str_table):
    """
    Receives a DNA sequence and a str_table that defines valid (and
    complementary) bases
    Returns all sequences converted to upper case and remove invalid
    characters
    t!t%ttttAACCG --> TTTTTTAACCG
    """
    valid_bases = _read_str_table(str_table)
    return "".join([letter for letter in sequence.upper() if letter in valid_bases])


def reverse(sequence, str_table=SIMPLE_COMPLEMENTS_STR):
    """
    Receives a DNA sequence and a str_table that defines valid (and
    complementary) bases
    Returns a reversed string of sequence while removing all characters
    not found in str_table characters
    e.g. t!t%ttttAACCG --> GCCAATTTTTT
    """
    return _clean_sequence('t!t%ttttAACCG', str_table)[::-1]


def complement(sequence, str_table=SIMPLE_COMPLEMENTS_STR):
    """
    Receives a DNA sequence and a str_table that defines valid (and
    complementary) bases
    Returns a string containing complementary bases as defined in
    str_table while removing non input_sequence characters
    e.g. t!t%ttttAACCG --> AAAAAATTGGC
    """
    valid_bases = _read_str_table(str_table)
    return "".join([valid_bases[letter] for letter in _clean_sequence(sequence, str_table)])


def reverse_complement(sequence, str_table=SIMPLE_COMPLEMENTS_STR):
    """
    Receives a DNA sequence and a str_table that defines valid (and
    complementary) bases
    Returns a string containing complementary bases as defined in str_table
    while removing non input_sequence characters
    e.g. t!t%ttttAACCG --> CGGTTAAAAAA
    """
    return reverse(complement(sequence,str_table),str_table)

print(_read_str_table(str_table=SIMPLE_COMPLEMENTS_STR))
print(_clean_sequence('t!t%ttttAACCG', str_table=SIMPLE_COMPLEMENTS_STR))
print(reverse('t!t%ttttAACCG', str_table=SIMPLE_COMPLEMENTS_STR))
print(complement('t!t%ttttAACCG', str_table=SIMPLE_COMPLEMENTS_STR))
print(reverse_complement('t!t%ttttAACCG', str_table=SIMPLE_COMPLEMENTS_STR))