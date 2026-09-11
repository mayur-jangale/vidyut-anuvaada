# Sutra प.7.1.5: आत्मनेपदेष्वनतः
# taddhita — continued

from sutra_engines import apply_general

SUTRA_CODE = "प.7.1.5"
SUTRA_TEXT = "आत्मनेपदेष्वनतः"
SUTRA_DESC = "taddhita — continued"


class Sutra715:
	def apply(self, word, pos):
		return apply_general(word, pos, SUTRA_CODE)

	EXAMPLES = [
	('अग्निः', '', 'प.7.1.5: अग्निः'),
		('रामः', '', 'प.7.1.5: रामः'),
		('सीता', '', 'प.7.1.5: सीता'),
	]

