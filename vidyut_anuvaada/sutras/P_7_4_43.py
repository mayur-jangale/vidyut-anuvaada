# Sutra प.7.4.43: जहातेश्च क्त्वि
# taddhita — continued

from sutra_engines import apply_general

SUTRA_CODE = "प.7.4.43"
SUTRA_TEXT = "जहातेश्च क्त्वि"
SUTRA_DESC = "taddhita — continued"


class Sutra7443:
	def apply(self, word, pos):
		return apply_general(word, pos, SUTRA_CODE)

	EXAMPLES = [
	('अग्निः', '', 'प.7.4.43: अग्निः'),
		('रामः', '', 'प.7.4.43: रामः'),
		('सीता', '', 'प.7.4.43: सीता'),
	]

