# Sutra प.6.2.124: कन्था च
# (Sandhi (euphonic combination)) — kanTA ca

from sutra_engines import apply_general

SUTRA_CODE = "प.6.2.124"
SUTRA_TEXT = "कन्था च"
SUTRA_DESC = "(Sandhi (euphonic combination)) — kanTA ca"


class Sutra62124:
	def apply(self, word, pos):
		return apply_general(word, pos, SUTRA_CODE)

	EXAMPLES = [
	('अग्निः', '', 'प.6.2.124: अग्निः'),
		('रामः', '', 'प.6.2.124: रामः'),
		('सीता', '', 'प.6.2.124: सीता'),
	]

