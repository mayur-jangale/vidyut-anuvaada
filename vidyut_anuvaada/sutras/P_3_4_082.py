# Sutra प82: parasmaipada Ralatu
# parasmaipadAnAM Ralatusu

from sutra_engines import apply_general
from P_3_4 import apply_3_4_82

SUTRA_CODE = "प82"
SUTRA_TEXT = "parasmaipada Ralatu"
SUTRA_DESC = "parasmaipadAnAM Ralatusu"


class Sutra3482:
	def apply(self, word, pos):
		return apply_3_4_82(word, pos)

	EXAMPLES = [
	('अग्निः', '', 'p34-082:parasmaipadAnAM Ralatusu;input=अग्निः;stem=अग्निः;ending=-;pos='),
		('रामः', '', 'p34-082:parasmaipadAnAM Ralatusu;input=रामः;stem=रामः;ending=-;pos='),
		('सीता', '', 'p34-082:parasmaipadAnAM Ralatusu;input=सीता;stem=सीता;ending=-;pos='),
	]

