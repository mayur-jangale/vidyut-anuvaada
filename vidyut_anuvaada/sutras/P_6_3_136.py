# Sutra प.6.3.136: निपातस्य च
# final-sandhi — continued

from sutra_engines import apply_general

SUTRA_CODE = "प.6.3.136"
SUTRA_TEXT = "निपातस्य च"
SUTRA_DESC = "final-sandhi — continued"


class Sutra63136:
	def apply(self, word, pos):
		return apply_general(word, pos, SUTRA_CODE)

	EXAMPLES = [
	('अग्निः', '', 'प.6.3.136: अग्निः'),
		('रामः', '', 'प.6.3.136: रामः'),
		('सीता', '', 'प.6.3.136: सीता'),
	]

