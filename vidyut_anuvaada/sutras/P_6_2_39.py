# Sutra प.6.2.39: क्षुल्लकश्च वैश्वदेवे
# hal-sandhi — continued

from sutra_engines import apply_general

SUTRA_CODE = "प.6.2.39"
SUTRA_TEXT = "क्षुल्लकश्च वैश्वदेवे"
SUTRA_DESC = "hal-sandhi — continued"


class Sutra6239:
	def apply(self, word, pos):
		return apply_general(word, pos, SUTRA_CODE)

	EXAMPLES = [
	('अग्निः', '', 'प.6.2.39: अग्निः'),
		('रामः', '', 'प.6.2.39: रामः'),
		('सीता', '', 'प.6.2.39: सीता'),
	]

