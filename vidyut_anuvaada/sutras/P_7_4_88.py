# Sutra प.7.4.88: उत् परस्यातः
# taddhita — continued

from sutra_engines import apply_general

SUTRA_CODE = "प.7.4.88"
SUTRA_TEXT = "उत् परस्यातः"
SUTRA_DESC = "taddhita — continued"


class Sutra7488:
	def apply(self, word, pos):
		return apply_general(word, pos, SUTRA_CODE)

	EXAMPLES = [
	('अग्निः', '', 'प.7.4.88: अग्निः'),
		('रामः', '', 'प.7.4.88: रामः'),
		('सीता', '', 'प.7.4.88: सीता'),
	]

