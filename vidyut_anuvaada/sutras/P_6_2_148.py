# Sutra प.6.2.148: कारकाद्दत्तश्रुतयोरेवाशिषि
# (Sandhi (euphonic combination)) — kArakAddattaSrutayorevASizi

from sutra_engines import apply_general

SUTRA_CODE = "प.6.2.148"
SUTRA_TEXT = "कारकाद्दत्तश्रुतयोरेवाशिषि"
SUTRA_DESC = "(Sandhi (euphonic combination)) — kArakAddattaSrutayorevASizi"


class Sutra62148:
	def apply(self, word, pos):
		return apply_general(word, pos, SUTRA_CODE)

	EXAMPLES = [
	('अग्निः', '', 'प.6.2.148: अग्निः'),
		('रामः', '', 'प.6.2.148: रामः'),
		('सीता', '', 'प.6.2.148: सीता'),
	]

