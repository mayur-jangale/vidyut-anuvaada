# Sutra प.7.4.74: ससूवेति निगमे
# taddhita — continued

from sutra_engines import apply_general

SUTRA_CODE = "प.7.4.74"
SUTRA_TEXT = "ससूवेति निगमे"
SUTRA_DESC = "taddhita — continued"


class Sutra7474:
	def apply(self, word, pos):
		return apply_general(word, pos, SUTRA_CODE)

	EXAMPLES = [
	('अग्निः', '', 'प.7.4.74: अग्निः'),
		('रामः', '', 'प.7.4.74: रामः'),
		('सीता', '', 'प.7.4.74: सीता'),
	]

