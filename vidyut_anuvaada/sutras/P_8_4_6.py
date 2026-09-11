# Sutra प.8.4.6: विभाषौषधिवनस्पतिभ्यः
# final transformations — continued

from sutra_engines import apply_general

SUTRA_CODE = "प.8.4.6"
SUTRA_TEXT = "विभाषौषधिवनस्पतिभ्यः"
SUTRA_DESC = "final transformations — continued"


class Sutra846:
	def apply(self, word, pos):
		return apply_general(word, pos, SUTRA_CODE)

	EXAMPLES = [
	('अग्निः', '', 'प.8.4.6: अग्निः'),
		('रामः', '', 'प.8.4.6: रामः'),
		('सीता', '', 'प.8.4.6: सीता'),
	]

