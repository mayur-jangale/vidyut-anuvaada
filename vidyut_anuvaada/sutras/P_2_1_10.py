# Sutra प.2.1.10: अक्षशलाकासंख्याः परिणा
# marker: akṣa-śalākā-count

from sutra_engines import apply_general

SUTRA_CODE = "प.2.1.10"
SUTRA_TEXT = "अक्षशलाकासंख्याः परिणा"
SUTRA_DESC = "akṣa-śalākā-count"


class Sutra2110:
 def apply(self, word, pos):
  from P_2_1 import apply_2_1_10
  return apply_2_1_10(word, pos)


 EXAMPLES = [
	('अग्निः', '', 'प.2.1.10:akṣa-śalākā-count;input=अग्निः;pos='),
		('रामः', '', 'प.2.1.10:akṣa-śalākā-count;input=रामः;pos='),
		('सीता', '', 'प.2.1.10:akṣa-śalākā-count;input=सीता;pos='),
	]
