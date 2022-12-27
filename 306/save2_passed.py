# TODO: Add imports
from Bio.Seq import Seq, CodonTable

import string

def translate_cds(cds: str, translation_table: str) -> str:
    """
    :param cds: str: DNA coding sequence (CDS)
    :param translation_table: str: translation table as defined in Bio.Seq.Seq.CodonTable.ambiguous_generic_by_name
    :return: str: Protein sequence
    """

    # TODO: Put your code here
    cds_clean = "".join([letter.upper() for letter in cds if letter.upper() in string.ascii_uppercase])
    return str(Seq.translate(Seq(cds_clean), table=CodonTable.ambiguous_generic_by_name[translation_table], cds=True))
    

print(translate_cds("ATGCCCGGGAAAGCGCACAAGAAGTGCTCAACGCCCCTACATCATCCGGGGTAA",
            "Vertebrate Mitochondrial"))

# "MPGKAHKKCSTPLHHPG"
