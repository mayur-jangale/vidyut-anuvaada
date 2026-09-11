# Sutra प.8.4.31: हलश्च इजुपधात्
# final transformations — continued

from sutra_engines import apply_general

SUTRA_CODE = "प.8.4.31"
SUTRA_TEXT = "हलश्च इजुपधात्"
SUTRA_DESC = "final transformations — continued"


class Sutra8431:
	def apply(self, word, pos):
		return apply_general(word, pos, SUTRA_CODE)

	EXAMPLES = [
	('अग्निः', '', 'प.8.4.31: अग्निः'),
		('रामः', '', 'प.8.4.31: रामः'),
		('सीता', '', 'प.8.4.31: सीता'),
	]

