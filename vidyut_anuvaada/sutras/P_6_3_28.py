# Sutra प.6.3.28: इद्वृद्धौ
# final-sandhi — continued

from sutra_engines import apply_general

SUTRA_CODE = "प.6.3.28"
SUTRA_TEXT = "इद्वृद्धौ"
SUTRA_DESC = "final-sandhi — continued"


class Sutra6328:
	def apply(self, word, pos):
		return apply_general(word, pos, SUTRA_CODE)

	EXAMPLES = [
	('अग्निः', '', 'प.6.3.28: अग्निः'),
		('रामः', '', 'प.6.3.28: रामः'),
		('सीता', '', 'प.6.3.28: सीता'),
	]

