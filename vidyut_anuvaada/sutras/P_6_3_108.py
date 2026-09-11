# Sutra प.6.3.108: पथि च च्छन्दसि
# final-sandhi — continued

from sutra_engines import apply_general

SUTRA_CODE = "प.6.3.108"
SUTRA_TEXT = "पथि च च्छन्दसि"
SUTRA_DESC = "final-sandhi — continued"


class Sutra63108:
	def apply(self, word, pos):
		return apply_general(word, pos, SUTRA_CODE)

	EXAMPLES = [
	('अग्निः', '', 'प.6.3.108: अग्निः'),
		('रामः', '', 'प.6.3.108: रामः'),
		('सीता', '', 'प.6.3.108: सीता'),
	]

