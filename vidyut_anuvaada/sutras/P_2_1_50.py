# Sutra प.2.1.50: दिक्संख्ये संज्ञायाम्
# marker: dik-saṃkhyā-saṃjñā

from sutra_engines import apply_general

SUTRA_CODE = "प.2.1.50"
SUTRA_TEXT = "दिक्संख्ये संज्ञायाम्"
SUTRA_DESC = "dik-saṃkhyā-saṃjñā"


class Sutra2150:
 def apply(self, word, pos):
  from P_2_1 import apply_2_1_50
  return apply_2_1_50(word, pos)


 EXAMPLES = [
	('अग्निः', '', 'प.2.1.50:dik-saṃkhyā-saṃjñā;input=अग्निः;pos='),
		('रामः', '', 'प.2.1.50:dik-saṃkhyā-saṃjñā;input=रामः;pos='),
		('सीता', '', 'प.2.1.50:dik-saṃkhyā-saṃjñā;input=सीता;pos='),
	]
