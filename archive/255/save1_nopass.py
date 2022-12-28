import os
from urllib.request import urlretrieve
from pprint import pprint
from collections import Counter

# Translation Table:
# https://www.ncbi.nlm.nih.gov/Taxonomy/Utils/wprintgc.cgi#SG11
# Each column represents one entry. Codon = {Base1}{Base2}{Base3}
# All Base 'T's need to be converted to 'U's to convert DNA to RNA
TRANSL_TABLE_11 = """
    AAs  = FFLLSSSSYY**CC*WLLLLPPPPHHQQRRRRIIIMTTTTNNKKSSRRVVVVAAAADDEEGGGG
  Starts = ---M------**--*----M------------MMMM---------------M------------
  Base1  = TTTTTTTTTTTTTTTTCCCCCCCCCCCCCCCCAAAAAAAAAAAAAAAAGGGGGGGGGGGGGGGG
  Base2  = TTTTCCCCAAAAGGGGTTTTCCCCAAAAGGGGTTTTCCCCAAAAGGGGTTTTCCCCAAAAGGGG
  Base3  = TCAGTCAGTCAGTCAGTCAGTCAGTCAGTCAGTCAGTCAGTCAGTCAGTCAGTCAGTCAGTCAG
"""

# Converted from http://ftp.ncbi.nlm.nih.gov/genomes/archive/old_refseq/Bacteria/Staphylococcus_aureus_Newman_uid58839/NC_009641.ffn  # noqa E501
URL = "https://bites-data.s3.us-east-2.amazonaws.com/NC_009641.txt"

# Order of bases in the table
BASE_ORDER = ["U", "C", "A", "G"]


def _preload_sequences(url=URL):
    """
    Provided helper function
    Returns coding sequences, one sequence each line
    """
    filename = os.path.join(os.getenv("TMP", "/tmp"), "NC_009641.txt")
    if not os.path.isfile(filename):
        urlretrieve(url, filename)
    with open(filename, "r") as f:
        return f.readlines()

def _preprocess_table(table_str):
    
    table_dict = dict((name.strip(), value.strip()) for name, value in 
        (tuple(line.split('=')) for line in table_str.strip().splitlines()))

    table_dict['Base1']=table_dict['Base1'].replace('T','U')
    table_dict['Base2']=table_dict['Base2'].replace('T','U')
    table_dict['Base3']=table_dict['Base3'].replace('T','U')

    return dict((''.join(line[1:4]), line[0]) for line in zip(
        table_dict['AAs'],table_dict['Base1'],table_dict['Base2'],table_dict['Base3']))


def return_codon_usage_table(
    sequences=_preload_sequences(), translation_table_str=TRANSL_TABLE_11
):
    """
    Receives a list of gene sequences and a translation table string
    Returns a string with all bases and their frequencies in a table
    with the following fields:
    codon_triplet: amino_acid_letter frequency_per_1000 absolute_occurrences

    Skip invalid coding sequences:
       --> must consist entirely of codons (3-base triplet)
    """
    chunks = []
    n = 3
    for sequence in sequences:
        chunks += [sequence[i:i+n] for i in range(0, len(sequence), n)]
    counter = Counter(chunks)
    total= sum(counter.values())
    translation_table = _preprocess_table(translation_table_str)
    unformatted_table = dict((codon, [aa, counter[codon]/total, counter[codon]]) \
        for codon, aa in translation_table.items())

    formatted_table = _format_table(unformatted_table, BASE_ORDER)
    return formatted_table

def _format_table(table, base_order):
    result = """
|  Codon AA  Freq  Count  |  Codon AA  Freq  Count  |  Codon AA  Freq  Count  |  Codon AA  Freq  Count  |
---------------------------------------------------------------------------------------------------------
|"""

    ITEM_SEP="|"
    LINE_SEP="|\n|"
    SEC_SEP="|\n"+104*"-"+"\n|"
    sections =[]
    for i in base_order:
        lines = []
        for k in base_order:
            items = []
            for j in base_order:
                codon="".join([i,j,k])
                aa=table[codon][0]
                freq=1000*table[codon][1]
                count=table[codon][2]
                items.append(f"  {codon}:  {aa} {freq:6.1f} {count:6}  ")
            lines.append(ITEM_SEP.join(items))
        sections.append(LINE_SEP.join(lines))
    result+= SEC_SEP.join(sections) + "|\n"+104*"-"+"\n"
    return result
if __name__ == "__main__":
    print(return_codon_usage_table())
    # _preprocess_table(TRANSL_TABLE_11)
    
"""
|  UUU:  F   32.6  26200
|  UUC:  F   12.1   9716
|  UUA:  L   53.6  43053

|  UUU:  F   32.7  26200  |  UCU:  S   12.9  10309  |  UAU:  Y   30.4  24332  |  UGU:  C    4.9   3919  |
|  UUC:  F   12.1   9716  |  UCC:  S    1.6   1310  |  UAC:  Y    8.6   6887  |  UGC:  C    1.2    992  |
"""
