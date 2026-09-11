# Sutra प.6.2.146: संज्ञायामनाचितादीनाम्
# (Sandhi (euphonic combination)) — saMjYAyAmanAcitAdInAm

from sutra_engines import apply_general

SUTRA_CODE = "प.6.2.146"
SUTRA_TEXT = "संज्ञायामनाचितादीनाम्"
SUTRA_DESC = "(Sandhi (euphonic combination)) — saMjYAyAmanAcitAdInAm"


class Sutra62146:
	def apply(self, word, pos):
		return apply_general(word, pos, SUTRA_CODE)

	EXAMPLES = [
	('अग्निः', '', 'प.6.2.146: अग्निः'),
		('रामः', '', 'प.6.2.146: रामः'),
		('सीता', '', 'प.6.2.146: सीता'),
	]

