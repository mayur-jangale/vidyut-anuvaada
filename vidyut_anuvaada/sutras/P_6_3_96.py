# Sutra प.6.3.96: सध मादस्थयोश्छन्दसि
# final-sandhi — continued

from sutra_engines import apply_general

SUTRA_CODE = "प.6.3.96"
SUTRA_TEXT = "सध मादस्थयोश्छन्दसि"
SUTRA_DESC = "final-sandhi — continued"


class Sutra6396:
	def apply(self, word, pos):
		return apply_general(word, pos, SUTRA_CODE)

	EXAMPLES = [
	('अग्निः', '', 'प.6.3.96: अग्निः'),
		('रामः', '', 'प.6.3.96: रामः'),
		('सीता', '', 'प.6.3.96: सीता'),
	]

