# Sutra प.7.4.47: अच उपसर्गात्तः
# taddhita — continued

from sutra_engines import apply_general

SUTRA_CODE = "प.7.4.47"
SUTRA_TEXT = "अच उपसर्गात्तः"
SUTRA_DESC = "taddhita — continued"


class Sutra7447:
	def apply(self, word, pos):
		return apply_general(word, pos, SUTRA_CODE)

	EXAMPLES = [
	('अग्निः', '', 'प.7.4.47: अग्निः'),
		('रामः', '', 'प.7.4.47: रामः'),
		('सीता', '', 'प.7.4.47: सीता'),
	]

