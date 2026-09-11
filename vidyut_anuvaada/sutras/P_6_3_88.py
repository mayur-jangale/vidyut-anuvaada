# Sutra प.6.3.88: विभाषोदरे
# final-sandhi — continued

from sutra_engines import apply_general

SUTRA_CODE = "प.6.3.88"
SUTRA_TEXT = "विभाषोदरे"
SUTRA_DESC = "final-sandhi — continued"


class Sutra6388:
	def apply(self, word, pos):
		return apply_general(word, pos, SUTRA_CODE)

	EXAMPLES = [
	('अग्निः', '', 'प.6.3.88: अग्निः'),
		('रामः', '', 'प.6.3.88: रामः'),
		('सीता', '', 'प.6.3.88: सीता'),
	]

