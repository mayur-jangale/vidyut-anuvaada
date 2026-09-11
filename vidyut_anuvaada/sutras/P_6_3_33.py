# Sutra प.6.3.33: पितरामातरा च च्छन्दसि
# final-sandhi — continued

from sutra_engines import apply_general

SUTRA_CODE = "प.6.3.33"
SUTRA_TEXT = "पितरामातरा च च्छन्दसि"
SUTRA_DESC = "final-sandhi — continued"


class Sutra6333:
	def apply(self, word, pos):
		return apply_general(word, pos, SUTRA_CODE)

	EXAMPLES = [
	('अग्निः', '', 'प.6.3.33: अग्निः'),
		('रामः', '', 'प.6.3.33: रामः'),
		('सीता', '', 'प.6.3.33: सीता'),
	]

