# Sutra प49: saptamyAM upapIqa ruDa
# saptamyAM ca upapIqa ruDa kfza

from sutra_engines import apply_general
from P_3_4 import apply_3_4_49

SUTRA_CODE = "प49"
SUTRA_TEXT = "saptamyAM upapIqa ruDa"
SUTRA_DESC = "saptamyAM ca upapIqa ruDa kfza"


class Sutra3449:
	def apply(self, word, pos):
		return apply_3_4_49(word, pos)

	EXAMPLES = [
	('अग्निः', '', 'p34-049:saptamyAM ca upapIqa ruDa kfza;input=अग्निः;stem=अग्निः;ending=-;pos='),
		('रामः', '', 'p34-049:saptamyAM ca upapIqa ruDa kfza;input=रामः;stem=रामः;ending=-;pos='),
		('सीता', '', 'p34-049:saptamyAM ca upapIqa ruDa kfza;input=सीता;stem=सीता;ending=-;pos='),
	]

