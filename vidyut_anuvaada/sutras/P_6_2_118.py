# Sutra प.6.2.118: क्रत्वादयश्च
# (Sandhi (euphonic combination)) — kratvAdayaSca

from sutra_engines import apply_general

SUTRA_CODE = "प.6.2.118"
SUTRA_TEXT = "क्रत्वादयश्च"
SUTRA_DESC = "(Sandhi (euphonic combination)) — kratvAdayaSca"


class Sutra62118:
	def apply(self, word, pos):
		return apply_general(word, pos, SUTRA_CODE)

	EXAMPLES = [
	('अग्निः', '', 'प.6.2.118: अग्निः'),
		('रामः', '', 'प.6.2.118: रामः'),
		('सीता', '', 'प.6.2.118: सीता'),
	]

