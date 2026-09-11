# Sutra प.6.2.181: न निविभ्याम्
# (Sandhi (euphonic combination)) — na niviByAm

from sutra_engines import apply_general

SUTRA_CODE = "प.6.2.181"
SUTRA_TEXT = "न निविभ्याम्"
SUTRA_DESC = "(Sandhi (euphonic combination)) — na niviByAm"


class Sutra62181:
	def apply(self, word, pos):
		return apply_general(word, pos, SUTRA_CODE)

	EXAMPLES = [
	('अग्निः', '', 'प.6.2.181: अग्निः'),
		('रामः', '', 'प.6.2.181: रामः'),
		('सीता', '', 'प.6.2.181: सीता'),
	]

