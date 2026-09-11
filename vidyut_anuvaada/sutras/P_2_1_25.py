# Sutra प.2.1.25: स्वयं क्तेन
# marker: svayaṃ-ktena

from sutra_engines import apply_general

SUTRA_CODE = "प.2.1.25"
SUTRA_TEXT = "स्वयं क्तेन"
SUTRA_DESC = "svayaṃ-ktena"


class Sutra2125:
 def apply(self, word, pos):
  from P_2_1 import apply_2_1_25
  return apply_2_1_25(word, pos)


 EXAMPLES = [
	('अग्निः', '', 'प.2.1.25:svayaṃ-ktena;input=अग्निः;pos='),
		('रामः', '', 'प.2.1.25:svayaṃ-ktena;input=रामः;pos='),
		('सीता', '', 'प.2.1.25:svayaṃ-ktena;input=सीता;pos='),
	]
