# Sutra प.2.1.63: कतरकतमौ जातिपरिप्रश्ने
# marker: katara-katamau

from sutra_engines import apply_general

SUTRA_CODE = "प.2.1.63"
SUTRA_TEXT = "कतरकतमौ जातिपरिप्रश्ने"
SUTRA_DESC = "katara-katamau"


class Sutra2163:
 def apply(self, word, pos):
  from P_2_1 import apply_2_1_63
  return apply_2_1_63(word, pos)


 EXAMPLES = [
	('अग्निः', '', 'प.2.1.63:katara-katamau;input=अग्निः;pos='),
		('रामः', '', 'प.2.1.63:katara-katamau;input=रामः;pos='),
		('सीता', '', 'प.2.1.63:katara-katamau;input=सीता;pos='),
	]
