# Sutra प.7.4.5: तिष्ठतेरित्
# taddhita — continued

from sutra_engines import apply_general

SUTRA_CODE = "प.7.4.5"
SUTRA_TEXT = "तिष्ठतेरित्"
SUTRA_DESC = "taddhita — continued"


class Sutra745:
	def apply(self, word, pos):
		return apply_general(word, pos, SUTRA_CODE)

	EXAMPLES = [
	('अग्निः', '', 'प.7.4.5: अग्निः'),
		('रामः', '', 'प.7.4.5: रामः'),
		('सीता', '', 'प.7.4.5: सीता'),
	]

