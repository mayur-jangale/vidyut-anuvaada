# Sutra प.3.4.80: थासस्से
# lit — perfect tense endings

from sutra_engines import apply_general

SUTRA_CODE = "प.3.4.80"
SUTRA_TEXT = "थासस्से"
SUTRA_DESC = "lit — perfect tense endings"


class Sutra3480:
	def apply(self, word, pos):
		return apply_general(word, pos, SUTRA_CODE)

	EXAMPLES = [
	('अग्निः', '', 'vikaraṇa: अग्निः'),
		('रामः', '', 'vikaraṇa: रामः'),
		('सीता', '', 'vikaraṇa: सीता'),
	]

