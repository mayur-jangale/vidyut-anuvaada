# Sutra प.2.1.15: अनुर्यत्समया
# marker: anuryat-samayā

from sutra_engines import apply_general

SUTRA_CODE = "प.2.1.15"
SUTRA_TEXT = "अनुर्यत्समया"
SUTRA_DESC = "anuryat-samayā"


class Sutra2115:
 def apply(self, word, pos):
  from P_2_1 import apply_2_1_15
  return apply_2_1_15(word, pos)


 EXAMPLES = [
	('अग्निः', '', 'प.2.1.15:anuryat-samayā;input=अग्निः;pos='),
		('रामः', '', 'प.2.1.15:anuryat-samayā;input=रामः;pos='),
		('सीता', '', 'प.2.1.15:anuryat-samayā;input=सीता;pos='),
	]
