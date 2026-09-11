# Sutra प.6.4.50: क्यस्य विभाषा
# samprasāraṇa — continued

from sutra_engines import apply_general

SUTRA_CODE = "प.6.4.50"
SUTRA_TEXT = "क्यस्य विभाषा"
SUTRA_DESC = "samprasāraṇa — continued"


class Sutra6450:
	def apply(self, word, pos):
		return apply_general(word, pos, SUTRA_CODE)

	EXAMPLES = [
	('अग्निः', '', 'प.6.4.50: अग्निः'),
		('रामः', '', 'प.6.4.50: रामः'),
		('सीता', '', 'प.6.4.50: सीता'),
	]

