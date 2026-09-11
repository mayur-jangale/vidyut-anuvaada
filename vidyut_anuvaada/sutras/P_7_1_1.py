# Sutra प.7.1.1: युवोरनाकौ
# taddhita — secondary derivations continued

from sutra_engines import apply_general

SUTRA_CODE = "प.7.1.1"
SUTRA_TEXT = "युवोरनाकौ"
SUTRA_DESC = "taddhita — secondary derivations continued"


class Sutra711:
	def apply(self, word, pos):
		return apply_general(word, pos, SUTRA_CODE)

	EXAMPLES = [
	('अग्निः', '', 'प.7.1.1: अग्निः'),
		('रामः', '', 'प.7.1.1: रामः'),
		('सीता', '', 'प.7.1.1: सीता'),
	]

