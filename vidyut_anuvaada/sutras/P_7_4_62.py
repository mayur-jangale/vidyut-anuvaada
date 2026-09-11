# Sutra प.7.4.62: कुहोश्चुः
# taddhita — continued

from sutra_engines import apply_general

SUTRA_CODE = "प.7.4.62"
SUTRA_TEXT = "कुहोश्चुः"
SUTRA_DESC = "taddhita — continued"


class Sutra7462:
	def apply(self, word, pos):
		return apply_general(word, pos, SUTRA_CODE)

	EXAMPLES = [
	('अग्निः', '', 'प.7.4.62: अग्निः'),
		('रामः', '', 'प.7.4.62: रामः'),
		('सीता', '', 'प.7.4.62: सीता'),
	]

