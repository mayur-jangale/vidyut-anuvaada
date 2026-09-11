# Sutra प.2.1.71: चतुष्पादो गर्भिण्या
# marker: catuṣpādo-garbhiṇyā

from sutra_engines import apply_general

SUTRA_CODE = "प.2.1.71"
SUTRA_TEXT = "चतुष्पादो गर्भिण्या"
SUTRA_DESC = "catuṣpādo-garbhiṇyā"


class Sutra2171:
 def apply(self, word, pos):
  from P_2_1 import apply_2_1_71
  return apply_2_1_71(word, pos)


 EXAMPLES = [
	('अग्निः', '', 'प.2.1.71:catuṣpādo-garbhiṇyā;input=अग्निः;pos='),
		('रामः', '', 'प.2.1.71:catuṣpādo-garbhiṇyā;input=रामः;pos='),
		('सीता', '', 'प.2.1.71:catuṣpādo-garbhiṇyā;input=सीता;pos='),
	]
