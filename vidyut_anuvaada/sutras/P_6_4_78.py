# Sutra प.6.4.78: अभ्यासस्यासवर्णे
# samprasāraṇa — continued

from sutra_engines import apply_general

SUTRA_CODE = "प.6.4.78"
SUTRA_TEXT = "अभ्यासस्यासवर्णे"
SUTRA_DESC = "samprasāraṇa — continued"


class Sutra6478:
	def apply(self, word, pos):
		return apply_general(word, pos, SUTRA_CODE)

	EXAMPLES = [
	('अग्निः', '', 'प.6.4.78: अग्निः'),
		('रामः', '', 'प.6.4.78: रामः'),
		('सीता', '', 'प.6.4.78: सीता'),
	]

