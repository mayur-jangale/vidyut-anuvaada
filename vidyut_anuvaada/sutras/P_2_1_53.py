# Sutra प.2.1.53: कुत्सितानि कुत्सनैः
# marker: kutsitāni-kutsanaiḥ

from sutra_engines import apply_general

SUTRA_CODE = "प.2.1.53"
SUTRA_TEXT = "कुत्सितानि कुत्सनैः"
SUTRA_DESC = "kutsitāni-kutsanaiḥ"


class Sutra2153:
 def apply(self, word, pos):
  from P_2_1 import apply_2_1_53
  return apply_2_1_53(word, pos)


 EXAMPLES = [
	('अग्निः', '', 'प.2.1.53:kutsitāni-kutsanaiḥ;input=अग्निः;pos='),
		('रामः', '', 'प.2.1.53:kutsitāni-kutsanaiḥ;input=रामः;pos='),
		('सीता', '', 'प.2.1.53:kutsitāni-kutsanaiḥ;input=सीता;pos='),
	]
