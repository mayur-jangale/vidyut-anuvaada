# Sutra प.7.4.17: अस्यतेस्थुक्
# taddhita — continued

from sutra_engines import apply_general

SUTRA_CODE = "प.7.4.17"
SUTRA_TEXT = "अस्यतेस्थुक्"
SUTRA_DESC = "taddhita — continued"


class Sutra7417:
	def apply(self, word, pos):
		return apply_general(word, pos, SUTRA_CODE)

	EXAMPLES = [
	('अग्निः', '', 'प.7.4.17: अग्निः'),
		('रामः', '', 'प.7.4.17: रामः'),
		('सीता', '', 'प.7.4.17: सीता'),
	]

