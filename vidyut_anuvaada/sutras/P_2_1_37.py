# Sutra प.2.1.37: पञ्चमी भयेन
# marker: pañcamī-bhaya

from sutra_engines import apply_general

SUTRA_CODE = "प.2.1.37"
SUTRA_TEXT = "पञ्चमी भयेन"
SUTRA_DESC = "pañcamī-bhaya"


class Sutra2137:
 def apply(self, word, pos):
  from P_2_1 import apply_2_1_37
  return apply_2_1_37(word, pos)


 EXAMPLES = [
	('अग्निः', '', 'प.2.1.37:pañcamī-bhaya;input=अग्निः;pos='),
		('रामः', '', 'प.2.1.37:pañcamī-bhaya;input=रामः;pos='),
		('सीता', '', 'प.2.1.37:pañcamī-bhaya;input=सीता;pos='),
	]
