# Sutra प.8.4.18: शेषे विभाषाऽकखादावषान्त उपदेशे
# final transformations — continued

from sutra_engines import apply_general

SUTRA_CODE = "प.8.4.18"
SUTRA_TEXT = "शेषे विभाषाऽकखादावषान्त उपदेशे"
SUTRA_DESC = "final transformations — continued"


class Sutra8418:
	def apply(self, word, pos):
		return apply_general(word, pos, SUTRA_CODE)

	EXAMPLES = [
	('अग्निः', '', 'प.8.4.18: अग्निः'),
		('रामः', '', 'प.8.4.18: रामः'),
		('सीता', '', 'प.8.4.18: सीता'),
	]

