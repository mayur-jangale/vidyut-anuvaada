# Sutra प.7.4.94: दीर्घो लघोः
# taddhita — continued

from sutra_engines import apply_general

SUTRA_CODE = "प.7.4.94"
SUTRA_TEXT = "दीर्घो लघोः"
SUTRA_DESC = "taddhita — continued"


class Sutra7494:
	def apply(self, word, pos):
		return apply_general(word, pos, SUTRA_CODE)

	EXAMPLES = [
	('अग्निः', '', 'प.7.4.94: अग्निः'),
		('रामः', '', 'प.7.4.94: रामः'),
		('सीता', '', 'प.7.4.94: सीता'),
	]

