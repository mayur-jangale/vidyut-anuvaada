# Sutra प.6.3.45: उगितश्च
# final-sandhi — continued

from sutra_engines import apply_general

SUTRA_CODE = "प.6.3.45"
SUTRA_TEXT = "उगितश्च"
SUTRA_DESC = "final-sandhi — continued"


class Sutra6345:
	def apply(self, word, pos):
		return apply_general(word, pos, SUTRA_CODE)

	EXAMPLES = [
	('अग्निः', '', 'प.6.3.45: अग्निः'),
		('रामः', '', 'प.6.3.45: रामः'),
		('सीता', '', 'प.6.3.45: सीता'),
	]

