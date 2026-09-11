# Sutra प.2.1.18: पारे मध्ये षष्ठ्या वा
# marker: pāre-madhye-ṣaṣṭhyā-vā

from sutra_engines import apply_general

SUTRA_CODE = "प.2.1.18"
SUTRA_TEXT = "पारे मध्ये षष्ठ्या वा"
SUTRA_DESC = "pāre-madhye-ṣaṣṭhyā-vā"


class Sutra2118:
 def apply(self, word, pos):
  from P_2_1 import apply_2_1_18
  return apply_2_1_18(word, pos)


 EXAMPLES = [
	('अग्निः', '', 'प.2.1.18:pāre-madhye-ṣaṣṭhyā-vā;input=अग्निः;pos='),
		('रामः', '', 'प.2.1.18:pāre-madhye-ṣaṣṭhyā-vā;input=रामः;pos='),
		('सीता', '', 'प.2.1.18:pāre-madhye-ṣaṣṭhyā-vā;input=सीता;pos='),
	]
