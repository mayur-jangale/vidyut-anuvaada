# Sutra प.7.2.7: अतो हलादेर्लघोः
# taddhita — continued

from sutra_engines import apply_general

SUTRA_CODE = "प.7.2.7"
SUTRA_TEXT = "अतो हलादेर्लघोः"
SUTRA_DESC = "taddhita — continued"


class Sutra727:
	def apply(self, word, pos):
		return apply_general(word, pos, SUTRA_CODE)

	EXAMPLES = [
	('अग्निः', '', 'प.7.2.7: अग्निः'),
		('रामः', '', 'प.7.2.7: रामः'),
		('सीता', '', 'प.7.2.7: सीता'),
	]

