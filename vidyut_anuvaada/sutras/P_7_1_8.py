# Sutra प.7.1.8: बहुलं छन्दसि
# taddhita — continued

from sutra_engines import apply_general

SUTRA_CODE = "प.7.1.8"
SUTRA_TEXT = "बहुलं छन्दसि"
SUTRA_DESC = "taddhita — continued"


class Sutra718:
	def apply(self, word, pos):
		return apply_general(word, pos, SUTRA_CODE)

	EXAMPLES = [
	('अग्निः', '', 'प.7.1.8: अग्निः'),
		('रामः', '', 'प.7.1.8: रामः'),
		('सीता', '', 'प.7.1.8: सीता'),
	]

