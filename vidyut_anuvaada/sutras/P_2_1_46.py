# Sutra प.2.1.46: तत्र
# marker: tatra-tatpuruṣa

from sutra_engines import apply_general

SUTRA_CODE = "प.2.1.46"
SUTRA_TEXT = "तत्र"
SUTRA_DESC = "tatra-tatpuruṣa"


class Sutra2146:
 def apply(self, word, pos):
  from P_2_1 import apply_2_1_46
  return apply_2_1_46(word, pos)


 EXAMPLES = [
	('अग्निः', '', 'प.2.1.46:tatra-tatpuruṣa;input=अग्निः;pos='),
		('रामः', '', 'प.2.1.46:tatra-tatpuruṣa;input=रामः;pos='),
		('सीता', '', 'प.2.1.46:tatra-tatpuruṣa;input=सीता;pos='),
	]
