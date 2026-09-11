# Sutra प.6.3.73: नलोपो नञः
# final-sandhi — continued

from sutra_engines import apply_general

SUTRA_CODE = "प.6.3.73"
SUTRA_TEXT = "नलोपो नञः"
SUTRA_DESC = "final-sandhi — continued"


class Sutra6373:
	def apply(self, word, pos):
		return apply_general(word, pos, SUTRA_CODE)

	EXAMPLES = [
	('अग्निः', '', 'प.6.3.73: अग्निः'),
		('रामः', '', 'प.6.3.73: रामः'),
		('सीता', '', 'प.6.3.73: सीता'),
	]

