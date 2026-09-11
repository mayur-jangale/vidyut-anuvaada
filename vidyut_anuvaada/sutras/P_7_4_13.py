# Sutra प.7.4.13: केऽणः
# taddhita — continued

from sutra_engines import apply_general

SUTRA_CODE = "प.7.4.13"
SUTRA_TEXT = "केऽणः"
SUTRA_DESC = "taddhita — continued"


class Sutra7413:
	def apply(self, word, pos):
		return apply_general(word, pos, SUTRA_CODE)

	EXAMPLES = [
	('अग्निः', '', 'प.7.4.13: अग्निः'),
		('रामः', '', 'प.7.4.13: रामः'),
		('सीता', '', 'प.7.4.13: सीता'),
	]

