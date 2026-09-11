# Sutra प.2.1.64: किं क्षेपे
# marker: kiṃ-kṣepe

from sutra_engines import apply_general

SUTRA_CODE = "प.2.1.64"
SUTRA_TEXT = "किं क्षेपे"
SUTRA_DESC = "kiṃ-kṣepe"


class Sutra2164:
 def apply(self, word, pos):
  from P_2_1 import apply_2_1_64
  return apply_2_1_64(word, pos)


 EXAMPLES = [
	('अग्निः', '', 'प.2.1.64:kiṃ-kṣepe;input=अग्निः;pos='),
		('रामः', '', 'प.2.1.64:kiṃ-kṣepe;input=रामः;pos='),
		('सीता', '', 'प.2.1.64:kiṃ-kṣepe;input=सीता;pos='),
	]
