# Sutra प.2.1.54: पापाणके कुत्सितैः
# marker: pāpāṇake-kutsitaiḥ

from sutra_engines import apply_general

SUTRA_CODE = "प.2.1.54"
SUTRA_TEXT = "पापाणके कुत्सितैः"
SUTRA_DESC = "pāpāṇake-kutsitaiḥ"


class Sutra2154:
 def apply(self, word, pos):
  from P_2_1 import apply_2_1_54
  return apply_2_1_54(word, pos)


 EXAMPLES = [
	('अग्निः', '', 'प.2.1.54:pāpāṇake-kutsitaiḥ;input=अग्निः;pos='),
		('रामः', '', 'प.2.1.54:pāpāṇake-kutsitaiḥ;input=रामः;pos='),
		('सीता', '', 'प.2.1.54:pāpāṇake-kutsitaiḥ;input=सीता;pos='),
	]
