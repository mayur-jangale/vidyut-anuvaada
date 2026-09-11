# Sutra प.7.1.3: झोऽन्तः
# taddhita — continued

from sutra_engines import apply_general

SUTRA_CODE = "प.7.1.3"
SUTRA_TEXT = "झोऽन्तः"
SUTRA_DESC = "taddhita — continued"


class Sutra713:
	def apply(self, word, pos):
		return apply_general(word, pos, SUTRA_CODE)

	EXAMPLES = [
	('अग्निः', '', 'प.7.1.3: अग्निः'),
		('रामः', '', 'प.7.1.3: रामः'),
		('सीता', '', 'प.7.1.3: सीता'),
	]

