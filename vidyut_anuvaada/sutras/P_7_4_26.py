# Sutra प.7.4.26: च्वौ च
# taddhita — continued

from sutra_engines import apply_general

SUTRA_CODE = "प.7.4.26"
SUTRA_TEXT = "च्वौ च"
SUTRA_DESC = "taddhita — continued"


class Sutra7426:
	def apply(self, word, pos):
		return apply_general(word, pos, SUTRA_CODE)

	EXAMPLES = [
	('अग्निः', '', 'प.7.4.26: अग्निः'),
		('रामः', '', 'प.7.4.26: रामः'),
		('सीता', '', 'प.7.4.26: सीता'),
	]

