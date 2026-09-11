# Sutra प.8.4.30: णेर्विभाषा
# final transformations — continued

from sutra_engines import apply_general

SUTRA_CODE = "प.8.4.30"
SUTRA_TEXT = "णेर्विभाषा"
SUTRA_DESC = "final transformations — continued"


class Sutra8430:
	def apply(self, word, pos):
		return apply_general(word, pos, SUTRA_CODE)

	EXAMPLES = [
	('अग्निः', '', 'प.8.4.30: अग्निः'),
		('रामः', '', 'प.8.4.30: रामः'),
		('सीता', '', 'प.8.4.30: सीता'),
	]

