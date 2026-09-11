# Sutra प.7.1.6: शीङो रुट्
# taddhita — continued

from sutra_engines import apply_general

SUTRA_CODE = "प.7.1.6"
SUTRA_TEXT = "शीङो रुट्"
SUTRA_DESC = "taddhita — continued"


class Sutra716:
	def apply(self, word, pos):
		return apply_general(word, pos, SUTRA_CODE)

	EXAMPLES = [
	('अग्निः', '', 'प.7.1.6: अग्निः'),
		('रामः', '', 'प.7.1.6: रामः'),
		('सीता', '', 'प.7.1.6: सीता'),
	]

