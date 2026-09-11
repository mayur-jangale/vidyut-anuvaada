# Sutra प.5.2.3: यवयवकषष्टिकाद्यत्
# taddhita — continued

from sutra_engines import apply_general

SUTRA_CODE = "प.5.2.3"
SUTRA_TEXT = "यवयवकषष्टिकाद्यत्"
SUTRA_DESC = "taddhita — continued"


class Sutra523:
	def apply(self, word, pos):
		return apply_general(word, pos, SUTRA_CODE)

	EXAMPLES = [
	('अग्निः', '', 'प.5.2.3: अग्निः'),
		('रामः', '', 'प.5.2.3: रामः'),
		('सीता', '', 'प.5.2.3: सीता'),
	]

