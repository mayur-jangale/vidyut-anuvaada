# Sutra प.6.2.79: णिनि
# hal-sandhi — continued

from sutra_engines import apply_general

SUTRA_CODE = "प.6.2.79"
SUTRA_TEXT = "णिनि"
SUTRA_DESC = "hal-sandhi — continued"


class Sutra6279:
	def apply(self, word, pos):
		return apply_general(word, pos, SUTRA_CODE)

	EXAMPLES = [
	('अग्निः', '', 'प.6.2.79: अग्निः'),
		('रामः', '', 'प.6.2.79: रामः'),
		('सीता', '', 'प.6.2.79: सीता'),
	]

