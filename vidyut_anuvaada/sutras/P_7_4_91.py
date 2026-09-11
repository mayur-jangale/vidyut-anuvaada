# Sutra प.7.4.91: रुग्रिकौ च लुकि
# taddhita — continued

from sutra_engines import apply_general

SUTRA_CODE = "प.7.4.91"
SUTRA_TEXT = "रुग्रिकौ च लुकि"
SUTRA_DESC = "taddhita — continued"


class Sutra7491:
	def apply(self, word, pos):
		return apply_general(word, pos, SUTRA_CODE)

	EXAMPLES = [
	('अग्निः', '', 'प.7.4.91: अग्निः'),
		('रामः', '', 'प.7.4.91: रामः'),
		('सीता', '', 'प.7.4.91: सीता'),
	]

