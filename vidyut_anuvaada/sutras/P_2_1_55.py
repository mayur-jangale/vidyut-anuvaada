# Sutra प.2.1.55: उपमानानि सामान्यवचनैः
# marker: upamānāni-sāmānyavacanaiḥ

from sutra_engines import apply_general

SUTRA_CODE = "प.2.1.55"
SUTRA_TEXT = "उपमानानि सामान्यवचनैः"
SUTRA_DESC = "upamānāni-sāmānyavacanaiḥ"


class Sutra2155:
 def apply(self, word, pos):
  from P_2_1 import apply_2_1_55
  return apply_2_1_55(word, pos)


 EXAMPLES = [
	('अग्निः', '', 'प.2.1.55:upamānāni-sāmānyavacanaiḥ;input=अग्निः;pos='),
		('रामः', '', 'प.2.1.55:upamānāni-sāmānyavacanaiḥ;input=रामः;pos='),
		('सीता', '', 'प.2.1.55:upamānāni-sāmānyavacanaiḥ;input=सीता;pos='),
	]
