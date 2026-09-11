# Sutra प22: ABIkzRye Ramul ca
# ABIkzRye Ramul ca

from sutra_engines import apply_general
from P_3_4 import apply_3_4_22

SUTRA_CODE = "प22"
SUTRA_TEXT = "ABIkzRye Ramul ca"
SUTRA_DESC = "ABIkzRye Ramul ca"


class Sutra3422:
	def apply(self, word, pos):
		return apply_3_4_22(word, pos)

	EXAMPLES = [
	('अग्निः', '', 'p34-022:ABIkzRye Ramul ca;input=अग्निः;stem=अग्निः;ending=-;pos='),
		('रामः', '', 'p34-022:ABIkzRye Ramul ca;input=रामः;stem=रामः;ending=-;pos='),
		('सीता', '', 'p34-022:ABIkzRye Ramul ca;input=सीता;stem=सीता;ending=-;pos='),
	]

