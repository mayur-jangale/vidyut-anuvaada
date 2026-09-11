# Sutra प.2.1.13: आङ् मर्यादाभिविध्योः
# marker: āṅ-maryādābhividhi

from sutra_engines import apply_general

SUTRA_CODE = "प.2.1.13"
SUTRA_TEXT = "आङ् मर्यादाभिविध्योः"
SUTRA_DESC = "āṅ-maryādābhividhi"


class Sutra2113:
 def apply(self, word, pos):
  from P_2_1 import apply_2_1_13
  return apply_2_1_13(word, pos)


 EXAMPLES = [
	('अग्निः', '', 'प.2.1.13:āṅ-maryādābhividhi;input=अग्निः;pos='),
		('रामः', '', 'प.2.1.13:āṅ-maryādābhividhi;input=रामः;pos='),
		('सीता', '', 'प.2.1.13:āṅ-maryādābhividhi;input=सीता;pos='),
	]
