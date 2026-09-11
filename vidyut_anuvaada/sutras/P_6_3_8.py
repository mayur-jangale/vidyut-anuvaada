# Sutra प.6.3.8: परस्य च
# final-sandhi — continued

from sutra_engines import apply_general

SUTRA_CODE = "प.6.3.8"
SUTRA_TEXT = "परस्य च"
SUTRA_DESC = "final-sandhi — continued"


class Sutra638:
	def apply(self, word, pos):
		return apply_general(word, pos, SUTRA_CODE)

	EXAMPLES = [
	('अग्निः', '', 'प.6.3.8: अग्निः'),
		('रामः', '', 'प.6.3.8: रामः'),
		('सीता', '', 'प.6.3.8: सीता'),
	]

