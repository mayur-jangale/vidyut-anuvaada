# Sutra प.2.1.60: क्तेन नञ्विशिष्टेनानञ्
# marker: ktena-nañ-viśiṣṭenānañ

from sutra_engines import apply_general

SUTRA_CODE = "प.2.1.60"
SUTRA_TEXT = "क्तेन नञ्विशिष्टेनानञ्"
SUTRA_DESC = "ktena-nañ-viśiṣṭenānañ"


class Sutra2160:
 def apply(self, word, pos):
  from P_2_1 import apply_2_1_60
  return apply_2_1_60(word, pos)


 EXAMPLES = [
	('अग्निः', '', 'प.2.1.60:ktena-nañ-viśiṣṭenānañ;input=अग्निः;pos='),
		('रामः', '', 'प.2.1.60:ktena-nañ-viśiṣṭenānañ;input=रामः;pos='),
		('सीता', '', 'प.2.1.60:ktena-nañ-viśiṣṭenānañ;input=सीता;pos='),
	]
