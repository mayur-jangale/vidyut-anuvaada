# Sutra प.6.2.99: पुरे प्राचाम्
# hal-sandhi — continued

from sutra_engines import apply_general

SUTRA_CODE = "प.6.2.99"
SUTRA_TEXT = "पुरे प्राचाम्"
SUTRA_DESC = "hal-sandhi — continued"


class Sutra6299:
	def apply(self, word, pos):
		return apply_general(word, pos, SUTRA_CODE)

	EXAMPLES = [
	('अग्निः', '', 'प.6.2.99: अग्निः'),
		('रामः', '', 'प.6.2.99: रामः'),
		('सीता', '', 'प.6.2.99: सीता'),
	]

