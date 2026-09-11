# Sutra प.6.3.76: एकादिश्चैकस्य चादुक्
# final-sandhi — continued

from sutra_engines import apply_general

SUTRA_CODE = "प.6.3.76"
SUTRA_TEXT = "एकादिश्चैकस्य चादुक्"
SUTRA_DESC = "final-sandhi — continued"


class Sutra6376:
	def apply(self, word, pos):
		return apply_general(word, pos, SUTRA_CODE)

	EXAMPLES = [
	('अग्निः', '', 'प.6.3.76: अग्निः'),
		('रामः', '', 'प.6.3.76: रामः'),
		('सीता', '', 'प.6.3.76: सीता'),
	]

