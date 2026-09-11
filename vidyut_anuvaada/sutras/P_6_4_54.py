# Sutra प.6.4.54: शमिता यज्ञे
# samprasāraṇa — continued

from sutra_engines import apply_general

SUTRA_CODE = "प.6.4.54"
SUTRA_TEXT = "शमिता यज्ञे"
SUTRA_DESC = "samprasāraṇa — continued"


class Sutra6454:
	def apply(self, word, pos):
		return apply_general(word, pos, SUTRA_CODE)

	EXAMPLES = [
	('अग्निः', '', 'प.6.4.54: अग्निः'),
		('रामः', '', 'प.6.4.54: रामः'),
		('सीता', '', 'प.6.4.54: सीता'),
	]

