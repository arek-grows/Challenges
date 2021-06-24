import unittest


def dna_to_rna(dna: str) -> str:
    DNA_to_mRNA = {'A': 'U', 'T': 'A', 'G': 'C', 'C': 'G'}
    end = ''
    for x in dna:
        end += DNA_to_mRNA[x]
    return end  # Put your code here!!!


class Tests(unittest.TestCase):
    def test_1(self):
        self.assertEqual(dna_to_rna("GCGTAC"), "CGCAUG")

    def test_2(self):
        self.assertEqual(dna_to_rna("ATTAGCGCGATATACGCGTAC"), "UAAUCGCGCUAUAUGCGCAUG")

    def test_3(self):
        self.assertEqual(dna_to_rna("CAGTATGCTGCAT"), "GUCAUACGACGUA")

    def test_4(self):
        self.assertEqual(dna_to_rna("CGATATA"), "GCUAUAU")

    def test_5(self):
        self.assertEqual(dna_to_rna("GCAGCTACA"), "CGUCGAUGU")


if __name__ == "__main__":
    unittest.main()