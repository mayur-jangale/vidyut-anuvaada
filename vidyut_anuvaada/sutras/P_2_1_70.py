# Sutra प.2.1.70: कुमारः श्रमणादिभिः
# marker: kumāraḥ-śramaṇādibhiḥ

from sutra_engines import apply_general

SUTRA_CODE = "प.2.1.70"
SUTRA_TEXT = "कुमारः श्रमणादिभिः"
SUTRA_DESC = "kumāraḥ-śramaṇādibhiḥ"


class Sutra2170:
 def apply(self, word, pos):
  from P_2_1 import apply_2_1_70
  return apply_2_1_70(word, pos)


 EXAMPLES = [
	('अग्निः', '', 'प.2.1.70:kumāraḥ-śramaṇādibhiḥ;input=अग्निः;pos='),
		('रामः', '', 'प.2.1.70:kumāraḥ-śramaṇādibhiḥ;input=रामः;pos='),
		('सीता', '', 'प.2.1.70:kumāraḥ-śramaṇādibhiḥ;input=सीता;pos='),
	]
