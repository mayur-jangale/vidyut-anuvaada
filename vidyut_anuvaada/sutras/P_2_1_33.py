# Sutra प.2.1.33: कृत्यैरधिकार्थवचने
# marker: kṛtyair-adhikārtha-vacane

from sutra_engines import apply_general

SUTRA_CODE = "प.2.1.33"
SUTRA_TEXT = "कृत्यैरधिकार्थवचने"
SUTRA_DESC = "kṛtyair-adhikārtha-vacane"


class Sutra2133:
 def apply(self, word, pos):
  from P_2_1 import apply_2_1_33
  return apply_2_1_33(word, pos)


 EXAMPLES = [
	('अग्निः', '', 'प.2.1.33:kṛtyair-adhikārtha-vacane;input=अग्निः;pos='),
		('रामः', '', 'प.2.1.33:kṛtyair-adhikārtha-vacane;input=रामः;pos='),
		('सीता', '', 'प.2.1.33:kṛtyair-adhikārtha-vacane;input=सीता;pos='),
	]
