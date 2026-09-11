# Sutra प.2.1.47: क्षेपे
# marker: kṣepa-tatpuruṣa

from sutra_engines import apply_general

SUTRA_CODE = "प.2.1.47"
SUTRA_TEXT = "क्षेपे"
SUTRA_DESC = "kṣepa-tatpuruṣa"


class Sutra2147:
 def apply(self, word, pos):
  from P_2_1 import apply_2_1_47
  return apply_2_1_47(word, pos)


 EXAMPLES = [
	('अग्निः', '', 'प.2.1.47:kṣepa-tatpuruṣa;input=अग्निः;pos='),
		('रामः', '', 'प.2.1.47:kṣepa-tatpuruṣa;input=रामः;pos='),
		('सीता', '', 'प.2.1.47:kṣepa-tatpuruṣa;input=सीता;pos='),
	]
