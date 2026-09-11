# Sutra प.5.2.94: तदस्यास्त्यस्मिन्निति मतुप्
# mat — possessive suffix (wealthy)

from sutra_engines import apply_general

SUTRA_CODE = "प.5.2.94"
SUTRA_TEXT = "तदस्यास्त्यस्मिन्निति मतुप्"
SUTRA_DESC = "mat — possessive suffix (wealthy)"


class Sutra5294:
	def apply(self, word, pos):
		return apply_general(word, pos, SUTRA_CODE)

	EXAMPLES = [
	('अग्निः', '', 'प.5.2.94: अग्निः'),
		('रामः', '', 'प.5.2.94: रामः'),
		('सीता', '', 'प.5.2.94: सीता'),
	]

