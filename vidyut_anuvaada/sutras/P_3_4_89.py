# Sutra प.3.4.89: मेर्निः
# lṛṅ — conditional endings

from sutra_engines import apply_general

SUTRA_CODE = "प.3.4.89"
SUTRA_TEXT = "मेर्निः"
SUTRA_DESC = "lṛṅ — conditional endings"


class Sutra3489:
	def apply(self, word, pos):
		return apply_general(word, pos, SUTRA_CODE)

	EXAMPLES = [
	('अग्निः', '', 'vikaraṇa: अग्निः'),
		('रामः', '', 'vikaraṇa: रामः'),
		('सीता', '', 'vikaraṇa: सीता'),
	]

