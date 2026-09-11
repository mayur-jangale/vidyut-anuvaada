# Sutra प.6.4.99: तनिपत्योश्छन्दसि
# samprasāraṇa — continued

from sutra_engines import apply_general

SUTRA_CODE = "प.6.4.99"
SUTRA_TEXT = "तनिपत्योश्छन्दसि"
SUTRA_DESC = "samprasāraṇa — continued"


class Sutra6499:
	def apply(self, word, pos):
		return apply_general(word, pos, SUTRA_CODE)

	EXAMPLES = [
	('अग्निः', '', 'प.6.4.99: अग्निः'),
		('रामः', '', 'प.6.4.99: रामः'),
		('सीता', '', 'प.6.4.99: सीता'),
	]

