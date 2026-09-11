# Sutra प.7.4.16: ऋदृशोऽङि गुणः
# taddhita — continued

from sutra_engines import apply_general

SUTRA_CODE = "प.7.4.16"
SUTRA_TEXT = "ऋदृशोऽङि गुणः"
SUTRA_DESC = "taddhita — continued"


class Sutra7416:
	def apply(self, word, pos):
		return apply_general(word, pos, SUTRA_CODE)

	EXAMPLES = [
	('अग्निः', '', 'प.7.4.16: अग्निः'),
		('रामः', '', 'प.7.4.16: रामः'),
		('सीता', '', 'प.7.4.16: सीता'),
	]

