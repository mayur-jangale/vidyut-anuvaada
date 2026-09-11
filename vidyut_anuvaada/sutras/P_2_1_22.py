# Sutra प.2.1.22: तत्पुरुषः
# marker: tatpuruṣaḥ

from sutra_engines import apply_general

SUTRA_CODE = "प.2.1.22"
SUTRA_TEXT = "तत्पुरुषः"
SUTRA_DESC = "tatpuruṣaḥ"


class Sutra2122:
 def apply(self, word, pos):
  from P_2_1 import apply_2_1_22
  return apply_2_1_22(word, pos)


 EXAMPLES = [
	('अग्निः', '', 'प.2.1.22:tatpuruṣaḥ;input=अग्निः;pos='),
		('रामः', '', 'प.2.1.22:tatpuruṣaḥ;input=रामः;pos='),
		('सीता', '', 'प.2.1.22:tatpuruṣaḥ;input=सीता;pos='),
	]
