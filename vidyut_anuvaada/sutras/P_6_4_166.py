# Sutra प.6.4.166: संयोगादिश्च
# (Sandhi (euphonic combination)) — saMyogAdiSca

from sutra_engines import apply_general

SUTRA_CODE = "प.6.4.166"
SUTRA_TEXT = "संयोगादिश्च"
SUTRA_DESC = "(Sandhi (euphonic combination)) — saMyogAdiSca"


class Sutra64166:
	def apply(self, word, pos):
		return apply_general(word, pos, SUTRA_CODE)

	EXAMPLES = [
	('अग्निः', '', 'प.6.4.166: अग्निः'),
		('रामः', '', 'प.6.4.166: रामः'),
		('सीता', '', 'प.6.4.166: सीता'),
	]

