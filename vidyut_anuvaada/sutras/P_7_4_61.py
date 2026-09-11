# Sutra प.7.4.61: शर्पूर्वाः खयः
# taddhita — continued

from sutra_engines import apply_general

SUTRA_CODE = "प.7.4.61"
SUTRA_TEXT = "शर्पूर्वाः खयः"
SUTRA_DESC = "taddhita — continued"


class Sutra7461:
	def apply(self, word, pos):
		return apply_general(word, pos, SUTRA_CODE)

	EXAMPLES = [
	('अग्निः', '', 'प.7.4.61: अग्निः'),
		('रामः', '', 'प.7.4.61: रामः'),
		('सीता', '', 'प.7.4.61: सीता'),
	]

