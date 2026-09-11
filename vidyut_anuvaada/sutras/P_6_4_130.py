# Sutra प.6.4.130: पादः पत्
# samprasāraṇa — continued

from sutra_engines import apply_general

SUTRA_CODE = "प.6.4.130"
SUTRA_TEXT = "पादः पत्"
SUTRA_DESC = "samprasāraṇa — continued"


class Sutra64130:
	def apply(self, word, pos):
		return apply_general(word, pos, SUTRA_CODE)

	EXAMPLES = [
	('अग्निः', '', 'प.6.4.130: अग्निः'),
		('रामः', '', 'प.6.4.130: रामः'),
		('सीता', '', 'प.6.4.130: सीता'),
	]

