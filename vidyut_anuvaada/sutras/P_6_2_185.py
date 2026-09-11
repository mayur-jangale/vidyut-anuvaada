# Sutra प.6.2.185: अभेर्मुखम्
# (Sandhi (euphonic combination)) — aBermuKam

from sutra_engines import apply_general

SUTRA_CODE = "प.6.2.185"
SUTRA_TEXT = "अभेर्मुखम्"
SUTRA_DESC = "(Sandhi (euphonic combination)) — aBermuKam"


class Sutra62185:
	def apply(self, word, pos):
		return apply_general(word, pos, SUTRA_CODE)

	EXAMPLES = [
	('अग्निः', '', 'प.6.2.185: अग्निः'),
		('रामः', '', 'प.6.2.185: रामः'),
		('सीता', '', 'प.6.2.185: सीता'),
	]

