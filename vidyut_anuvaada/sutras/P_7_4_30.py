# Sutra प.7.4.30: यङि च
# taddhita — continued

from sutra_engines import apply_general

SUTRA_CODE = "प.7.4.30"
SUTRA_TEXT = "यङि च"
SUTRA_DESC = "taddhita — continued"


class Sutra7430:
	def apply(self, word, pos):
		return apply_general(word, pos, SUTRA_CODE)

	EXAMPLES = [
	('अग्निः', '', 'प.7.4.30: अग्निः'),
		('रामः', '', 'प.7.4.30: रामः'),
		('सीता', '', 'प.7.4.30: सीता'),
	]

