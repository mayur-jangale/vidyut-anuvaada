# Sutra प.7.4.44: विभाषा छन्दसि
# taddhita — continued

from sutra_engines import apply_general

SUTRA_CODE = "प.7.4.44"
SUTRA_TEXT = "विभाषा छन्दसि"
SUTRA_DESC = "taddhita — continued"


class Sutra7444:
	def apply(self, word, pos):
		return apply_general(word, pos, SUTRA_CODE)

	EXAMPLES = [
	('अग्निः', '', 'प.7.4.44: अग्निः'),
		('रामः', '', 'प.7.4.44: रामः'),
		('सीता', '', 'प.7.4.44: सीता'),
	]

