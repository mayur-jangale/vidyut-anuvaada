# Sutra प.6.3.106: विभाषा पुरुषे
# final-sandhi — continued

from sutra_engines import apply_general

SUTRA_CODE = "प.6.3.106"
SUTRA_TEXT = "विभाषा पुरुषे"
SUTRA_DESC = "final-sandhi — continued"


class Sutra63106:
	def apply(self, word, pos):
		return apply_general(word, pos, SUTRA_CODE)

	EXAMPLES = [
	('अग्निः', '', 'प.6.3.106: अग्निः'),
		('रामः', '', 'प.6.3.106: रामः'),
		('सीता', '', 'प.6.3.106: सीता'),
	]

