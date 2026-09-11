# Sutra प.7.1.10: बहुलं छन्दसि
# taddhita — continued

from sutra_engines import apply_general

SUTRA_CODE = "प.7.1.10"
SUTRA_TEXT = "बहुलं छन्दसि"
SUTRA_DESC = "taddhita — continued"


class Sutra7110:
	def apply(self, word, pos):
		return apply_general(word, pos, SUTRA_CODE)

	EXAMPLES = [
	('अग्निः', '', 'प.7.1.10: अग्निः'),
		('रामः', '', 'प.7.1.10: रामः'),
		('सीता', '', 'प.7.1.10: सीता'),
	]

