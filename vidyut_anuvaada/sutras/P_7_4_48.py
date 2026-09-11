# Sutra प.7.4.48: अपो भि
# taddhita — continued

from sutra_engines import apply_general

SUTRA_CODE = "प.7.4.48"
SUTRA_TEXT = "अपो भि"
SUTRA_DESC = "taddhita — continued"


class Sutra7448:
	def apply(self, word, pos):
		return apply_general(word, pos, SUTRA_CODE)

	EXAMPLES = [
	('अग्निः', '', 'प.7.4.48: अग्निः'),
		('रामः', '', 'प.7.4.48: रामः'),
		('सीता', '', 'प.7.4.48: सीता'),
	]

