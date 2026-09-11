# Sutra प.6.2.130: अकर्मधारये राज्यम्
# (Sandhi (euphonic combination)) — akarmaDAraye rAjyam

from sutra_engines import apply_general

SUTRA_CODE = "प.6.2.130"
SUTRA_TEXT = "अकर्मधारये राज्यम्"
SUTRA_DESC = "(Sandhi (euphonic combination)) — akarmaDAraye rAjyam"


class Sutra62130:
	def apply(self, word, pos):
		return apply_general(word, pos, SUTRA_CODE)

	EXAMPLES = [
	('अग्निः', '', 'प.6.2.130: अग्निः'),
		('रामः', '', 'प.6.2.130: रामः'),
		('सीता', '', 'प.6.2.130: सीता'),
	]

