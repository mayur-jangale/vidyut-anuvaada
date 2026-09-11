# Sutra प.2.1.28: कालाः
# marker: kāla-tatpuruṣa

from sutra_engines import apply_general

SUTRA_CODE = "प.2.1.28"
SUTRA_TEXT = "कालाः"
SUTRA_DESC = "kāla-tatpuruṣa"


class Sutra2128:
 def apply(self, word, pos):
  from P_2_1 import apply_2_1_28
  return apply_2_1_28(word, pos)


 EXAMPLES = [
	('अग्निः', '', 'प.2.1.28:kāla-tatpuruṣa;input=अग्निः;pos='),
		('रामः', '', 'प.2.1.28:kāla-tatpuruṣa;input=रामः;pos='),
		('सीता', '', 'प.2.1.28:kāla-tatpuruṣa;input=सीता;pos='),
	]
