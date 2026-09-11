# Sutra प.2.1.59: श्रेण्यादयः कृतादिभिः
# marker: śreṇyādayaḥ-kṛtādibhiḥ

from sutra_engines import apply_general

SUTRA_CODE = "प.2.1.59"
SUTRA_TEXT = "श्रेण्यादयः कृतादिभिः"
SUTRA_DESC = "śreṇyādayaḥ-kṛtādibhiḥ"


class Sutra2159:
 def apply(self, word, pos):
  from P_2_1 import apply_2_1_59
  return apply_2_1_59(word, pos)


 EXAMPLES = [
	('अग्निः', '', 'प.2.1.59:śreṇyādayaḥ-kṛtādibhiḥ;input=अग्निः;pos='),
		('रामः', '', 'प.2.1.59:śreṇyādayaḥ-kṛtādibhiḥ;input=रामः;pos='),
		('सीता', '', 'प.2.1.59:śreṇyādayaḥ-kṛtādibhiḥ;input=सीता;pos='),
	]
