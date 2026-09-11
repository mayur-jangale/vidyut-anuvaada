# Sutra प.6.2.102: कुसूलकूपकुम्भशालं बिले
# (Sandhi (euphonic combination)) — kusUlakUpakumBaSAlaM bile

from sutra_engines import apply_general

SUTRA_CODE = "प.6.2.102"
SUTRA_TEXT = "कुसूलकूपकुम्भशालं बिले"
SUTRA_DESC = "(Sandhi (euphonic combination)) — kusUlakUpakumBaSAlaM bile"


class Sutra62102:
	def apply(self, word, pos):
		return apply_general(word, pos, SUTRA_CODE)

	EXAMPLES = [
	('अग्निः', '', 'प.6.2.102: अग्निः'),
		('रामः', '', 'प.6.2.102: रामः'),
		('सीता', '', 'प.6.2.102: सीता'),
	]

