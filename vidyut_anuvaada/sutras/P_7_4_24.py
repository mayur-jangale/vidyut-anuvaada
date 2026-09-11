# Sutra प.7.4.24: एतेर्लिङि
# taddhita — continued

from sutra_engines import apply_general

SUTRA_CODE = "प.7.4.24"
SUTRA_TEXT = "एतेर्लिङि"
SUTRA_DESC = "taddhita — continued"


class Sutra7424:
	def apply(self, word, pos):
		return apply_general(word, pos, SUTRA_CODE)

	EXAMPLES = [
	('अग्निः', '', 'प.7.4.24: अग्निः'),
		('रामः', '', 'प.7.4.24: रामः'),
		('सीता', '', 'प.7.4.24: सीता'),
	]

