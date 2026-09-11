# Sutra प.7.2.9: तितुत्रतथसिसुसरकसेषु च
# taddhita — continued

from sutra_engines import apply_general

SUTRA_CODE = "प.7.2.9"
SUTRA_TEXT = "तितुत्रतथसिसुसरकसेषु च"
SUTRA_DESC = "taddhita — continued"


class Sutra729:
	def apply(self, word, pos):
		return apply_general(word, pos, SUTRA_CODE)

	EXAMPLES = [
	('अग्निः', '', 'प.7.2.9: अग्निः'),
		('रामः', '', 'प.7.2.9: रामः'),
		('सीता', '', 'प.7.2.9: सीता'),
	]

