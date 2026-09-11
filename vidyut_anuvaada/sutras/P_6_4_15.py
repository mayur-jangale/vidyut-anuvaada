# Sutra प.6.4.15: अनुनासिकस्य क्विझलोः क्ङिति
# samprasāraṇa — continued

from sutra_engines import apply_general

SUTRA_CODE = "प.6.4.15"
SUTRA_TEXT = "अनुनासिकस्य क्विझलोः क्ङिति"
SUTRA_DESC = "samprasāraṇa — continued"


class Sutra6415:
	def apply(self, word, pos):
		return apply_general(word, pos, SUTRA_CODE)

	EXAMPLES = [
	('अग्निः', '', 'प.6.4.15: अग्निः'),
		('रामः', '', 'प.6.4.15: रामः'),
		('सीता', '', 'प.6.4.15: सीता'),
	]

