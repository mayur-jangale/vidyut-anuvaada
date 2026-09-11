# Sutra प.2.1.48: पात्रेसमितादयश्च
# marker: pātra-samita

from sutra_engines import apply_general

SUTRA_CODE = "प.2.1.48"
SUTRA_TEXT = "पात्रेसमितादयश्च"
SUTRA_DESC = "pātra-samita"


class Sutra2148:
 def apply(self, word, pos):
  from P_2_1 import apply_2_1_48
  return apply_2_1_48(word, pos)


 EXAMPLES = [
	('अग्निः', '', 'प.2.1.48:pātra-samita;input=अग्निः;pos='),
		('रामः', '', 'प.2.1.48:pātra-samita;input=रामः;pos='),
		('सीता', '', 'प.2.1.48:pātra-samita;input=सीता;pos='),
	]
