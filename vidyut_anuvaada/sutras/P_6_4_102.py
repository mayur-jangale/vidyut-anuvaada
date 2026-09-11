# Sutra प.6.4.102: श्रुशृणुपॄकृवृभ्यश्छन्दसि
# samprasāraṇa — continued

from sutra_engines import apply_general

SUTRA_CODE = "प.6.4.102"
SUTRA_TEXT = "श्रुशृणुपॄकृवृभ्यश्छन्दसि"
SUTRA_DESC = "samprasāraṇa — continued"


class Sutra64102:
	def apply(self, word, pos):
		return apply_general(word, pos, SUTRA_CODE)

	EXAMPLES = [
	('अग्निः', '', 'प.6.4.102: अग्निः'),
		('रामः', '', 'प.6.4.102: रामः'),
		('सीता', '', 'प.6.4.102: सीता'),
	]

