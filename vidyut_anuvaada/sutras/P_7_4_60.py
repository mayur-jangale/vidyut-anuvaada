# Sutra प.7.4.60: हलादिः शेषः
# taddhita — continued

from sutra_engines import apply_general

SUTRA_CODE = "प.7.4.60"
SUTRA_TEXT = "हलादिः शेषः"
SUTRA_DESC = "taddhita — continued"


class Sutra7460:
	def apply(self, word, pos):
		return apply_general(word, pos, SUTRA_CODE)

	EXAMPLES = [
	('अग्निः', '', 'प.7.4.60: अग्निः'),
		('रामः', '', 'प.7.4.60: रामः'),
		('सीता', '', 'प.7.4.60: सीता'),
	]

