# Sutra प.8.4.11: प्रातिपदिकान्तनुम्विभक्तिषु च
# final transformations — continued

from sutra_engines import apply_general

SUTRA_CODE = "प.8.4.11"
SUTRA_TEXT = "प्रातिपदिकान्तनुम्विभक्तिषु च"
SUTRA_DESC = "final transformations — continued"


class Sutra8411:
	def apply(self, word, pos):
		return apply_general(word, pos, SUTRA_CODE)

	EXAMPLES = [
	('अग्निः', '', 'प.8.4.11: अग्निः'),
		('रामः', '', 'प.8.4.11: रामः'),
		('सीता', '', 'प.8.4.11: सीता'),
	]

