# Sutra प.7.4.73: भवतेरः
# taddhita — continued

from sutra_engines import apply_general

SUTRA_CODE = "प.7.4.73"
SUTRA_TEXT = "भवतेरः"
SUTRA_DESC = "taddhita — continued"


class Sutra7473:
	def apply(self, word, pos):
		return apply_general(word, pos, SUTRA_CODE)

	EXAMPLES = [
	('अग्निः', '', 'प.7.4.73: अग्निः'),
		('रामः', '', 'प.7.4.73: रामः'),
		('सीता', '', 'प.7.4.73: सीता'),
	]

