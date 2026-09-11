# Sutra प.7.4.59: ह्रस्वः
# taddhita — continued

from sutra_engines import apply_general

SUTRA_CODE = "प.7.4.59"
SUTRA_TEXT = "ह्रस्वः"
SUTRA_DESC = "taddhita — continued"


class Sutra7459:
	def apply(self, word, pos):
		return apply_general(word, pos, SUTRA_CODE)

	EXAMPLES = [
	('अग्निः', '', 'प.7.4.59: अग्निः'),
		('रामः', '', 'प.7.4.59: रामः'),
		('सीता', '', 'प.7.4.59: सीता'),
	]

