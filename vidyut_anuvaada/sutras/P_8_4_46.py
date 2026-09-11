# Sutra प.8.4.46: अचो रहाभ्यां द्वे
# final transformations — continued

from sutra_engines import apply_general

SUTRA_CODE = "प.8.4.46"
SUTRA_TEXT = "अचो रहाभ्यां द्वे"
SUTRA_DESC = "final transformations — continued"


class Sutra8446:
	def apply(self, word, pos):
		return apply_general(word, pos, SUTRA_CODE)

	EXAMPLES = [
	('अग्निः', '', 'प.8.4.46: अग्निः'),
		('रामः', '', 'प.8.4.46: रामः'),
		('सीता', '', 'प.8.4.46: सीता'),
	]

