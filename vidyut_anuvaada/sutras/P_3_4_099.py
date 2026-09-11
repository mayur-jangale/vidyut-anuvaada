# Sutra प99: nityaM NitaH
# nityaM NitaH

from sutra_engines import apply_general
from P_3_4 import apply_3_4_99

SUTRA_CODE = "प99"
SUTRA_TEXT = "nityaM NitaH"
SUTRA_DESC = "nityaM NitaH"


class Sutra3499:
	def apply(self, word, pos):
		return apply_3_4_99(word, pos)

	EXAMPLES = [
	('अग्निः', '', 'p34-099:nityaM NitaH;input=अग्निः;stem=अग्निः;ending=-;pos='),
		('रामः', '', 'p34-099:nityaM NitaH;input=रामः;stem=रामः;ending=-;pos='),
		('सीता', '', 'p34-099:nityaM NitaH;input=सीता;stem=सीता;ending=-;pos='),
	]

