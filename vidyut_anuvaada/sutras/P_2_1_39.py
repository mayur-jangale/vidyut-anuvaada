# Sutra प.2.1.39: स्तोकान्तिकदूरार्थकृच्छ्राणि क्तेन
# marker: stoka-antika-dūra-ktā

from sutra_engines import apply_general

SUTRA_CODE = "प.2.1.39"
SUTRA_TEXT = "स्तोकान्तिकदूरार्थकृच्छ्राणि क्तेन"
SUTRA_DESC = "stoka-antika-dūra-ktā"


class Sutra2139:
 def apply(self, word, pos):
  from P_2_1 import apply_2_1_39
  return apply_2_1_39(word, pos)


 EXAMPLES = [
	('अग्निः', '', 'प.2.1.39:stoka-antika-dūra-ktā;input=अग्निः;pos='),
		('रामः', '', 'प.2.1.39:stoka-antika-dūra-ktā;input=रामः;pos='),
		('सीता', '', 'प.2.1.39:stoka-antika-dūra-ktā;input=सीता;pos='),
	]
