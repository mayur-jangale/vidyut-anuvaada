# Sutra प.5.1.8: अजाविभ्यां थ्यन्
# strīpratyaya — continued

from sutra_engines import apply_general

SUTRA_CODE = "प.5.1.8"
SUTRA_TEXT = "अजाविभ्यां थ्यन्"
SUTRA_DESC = "strīpratyaya — continued"


class Sutra518:
	def apply(self, word, pos):
		return apply_general(word, pos, SUTRA_CODE)

	EXAMPLES = [
	('अग्निः', '', 'प.5.1.8: अग्निः'),
		('रामः', '', 'प.5.1.8: रामः'),
		('सीता', '', 'प.5.1.8: सीता'),
	]

