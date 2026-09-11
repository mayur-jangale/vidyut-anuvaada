# Sutra प.2.1.11: विभाषा
# marker: vibhāṣā

from sutra_engines import apply_general

SUTRA_CODE = "प.2.1.11"
SUTRA_TEXT = "विभाषा"
SUTRA_DESC = "vibhāṣā"


class Sutra2111:
 def apply(self, word, pos):
  from P_2_1 import apply_2_1_11
  return apply_2_1_11(word, pos)


 EXAMPLES = [
	('अग्निः', '', 'प.2.1.11:vibhāṣā;input=अग्निः;pos='),
		('रामः', '', 'प.2.1.11:vibhāṣā;input=रामः;pos='),
		('सीता', '', 'प.2.1.11:vibhāṣā;input=सीता;pos='),
	]
