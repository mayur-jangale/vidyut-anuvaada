# Sutra प.7.1.4: अदभ्यस्तात्
# taddhita — continued

from sutra_engines import apply_general

SUTRA_CODE = "प.7.1.4"
SUTRA_TEXT = "अदभ्यस्तात्"
SUTRA_DESC = "taddhita — continued"


class Sutra714:
	def apply(self, word, pos):
		return apply_general(word, pos, SUTRA_CODE)

	EXAMPLES = [
	('अग्निः', '', 'प.7.1.4: अग्निः'),
		('रामः', '', 'प.7.1.4: रामः'),
		('सीता', '', 'प.7.1.4: सीता'),
	]

