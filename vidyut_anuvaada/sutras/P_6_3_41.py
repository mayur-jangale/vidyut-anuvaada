# Sutra प.6.3.41: जातेश्च
# final-sandhi — continued

from sutra_engines import apply_general

SUTRA_CODE = "प.6.3.41"
SUTRA_TEXT = "जातेश्च"
SUTRA_DESC = "final-sandhi — continued"


class Sutra6341:
	def apply(self, word, pos):
		return apply_general(word, pos, SUTRA_CODE)

	EXAMPLES = [
	('अग्निः', '', 'प.6.3.41: अग्निः'),
		('रामः', '', 'प.6.3.41: रामः'),
		('सीता', '', 'प.6.3.41: सीता'),
	]

