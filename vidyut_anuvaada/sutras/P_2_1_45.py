# Sutra प.2.1.45: क्तेनाहोरात्रावयवाः
# marker: ktena-ahorātra

from sutra_engines import apply_general

SUTRA_CODE = "प.2.1.45"
SUTRA_TEXT = "क्तेनाहोरात्रावयवाः"
SUTRA_DESC = "ktena-ahorātra"


class Sutra2145:
 def apply(self, word, pos):
  from P_2_1 import apply_2_1_45
  return apply_2_1_45(word, pos)


 EXAMPLES = [
	('अग्निः', '', 'प.2.1.45:ktena-ahorātra;input=अग्निः;pos='),
		('रामः', '', 'प.2.1.45:ktena-ahorātra;input=रामः;pos='),
		('सीता', '', 'प.2.1.45:ktena-ahorātra;input=सीता;pos='),
	]
