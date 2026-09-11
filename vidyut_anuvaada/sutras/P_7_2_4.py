# Sutra प.7.2.4: नेटि
# taddhita — continued

from sutra_engines import apply_general

SUTRA_CODE = "प.7.2.4"
SUTRA_TEXT = "नेटि"
SUTRA_DESC = "taddhita — continued"


class Sutra724:
	def apply(self, word, pos):
		return apply_general(word, pos, SUTRA_CODE)

	EXAMPLES = [
	('अग्निः', '', 'प.7.2.4: अग्निः'),
		('रामः', '', 'प.7.2.4: रामः'),
		('सीता', '', 'प.7.2.4: सीता'),
	]

