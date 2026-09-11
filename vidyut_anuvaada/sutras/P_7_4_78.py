# Sutra प.7.4.78: बहुलं छन्दसि
# taddhita — continued

from sutra_engines import apply_general

SUTRA_CODE = "प.7.4.78"
SUTRA_TEXT = "बहुलं छन्दसि"
SUTRA_DESC = "taddhita — continued"


class Sutra7478:
	def apply(self, word, pos):
		return apply_general(word, pos, SUTRA_CODE)

	EXAMPLES = [
	('अग्निः', '', 'प.7.4.78: अग्निः'),
		('रामः', '', 'प.7.4.78: रामः'),
		('सीता', '', 'प.7.4.78: सीता'),
	]

