# Sutra प.2.1.43: कृत्यैरृणे
# marker: kṛtyair-ṛṇe

from sutra_engines import apply_general

SUTRA_CODE = "प.2.1.43"
SUTRA_TEXT = "कृत्यैरृणे"
SUTRA_DESC = "kṛtyair-ṛṇe"


class Sutra2143:
 def apply(self, word, pos):
  from P_2_1 import apply_2_1_43
  return apply_2_1_43(word, pos)


 EXAMPLES = [
	('अग्निः', '', 'प.2.1.43:kṛtyair-ṛṇe;input=अग्निः;pos='),
		('रामः', '', 'प.2.1.43:kṛtyair-ṛṇe;input=रामः;pos='),
		('सीता', '', 'प.2.1.43:kṛtyair-ṛṇe;input=सीता;pos='),
	]
