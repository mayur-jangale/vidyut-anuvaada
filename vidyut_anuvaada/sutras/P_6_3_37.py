# Sutra प.6.3.37: न कोपधायाः
# final-sandhi — continued

from sutra_engines import apply_general

SUTRA_CODE = "प.6.3.37"
SUTRA_TEXT = "न कोपधायाः"
SUTRA_DESC = "final-sandhi — continued"


class Sutra6337:
	def apply(self, word, pos):
		return apply_general(word, pos, SUTRA_CODE)

	EXAMPLES = [
	('अग्निः', '', 'प.6.3.37: अग्निः'),
		('रामः', '', 'प.6.3.37: रामः'),
		('सीता', '', 'प.6.3.37: सीता'),
	]

