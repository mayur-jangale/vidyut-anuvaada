# Sutra प.6.2.159: संज्ञायाम्
# (Sandhi (euphonic combination)) — saMjYAyAm

from sutra_engines import apply_general

SUTRA_CODE = "प.6.2.159"
SUTRA_TEXT = "संज्ञायाम्"
SUTRA_DESC = "(Sandhi (euphonic combination)) — saMjYAyAm"


class Sutra62159:
	def apply(self, word, pos):
		return apply_general(word, pos, SUTRA_CODE)

	EXAMPLES = [
	('अग्निः', '', 'प.6.2.159: अग्निः'),
		('रामः', '', 'प.6.2.159: रामः'),
		('सीता', '', 'प.6.2.159: सीता'),
	]

