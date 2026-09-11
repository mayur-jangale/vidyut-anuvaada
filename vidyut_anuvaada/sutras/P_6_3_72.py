# Sutra प.6.3.72: रात्रेः कृति विभाषा
# final-sandhi — continued

from sutra_engines import apply_general

SUTRA_CODE = "प.6.3.72"
SUTRA_TEXT = "रात्रेः कृति विभाषा"
SUTRA_DESC = "final-sandhi — continued"


class Sutra6372:
	def apply(self, word, pos):
		return apply_general(word, pos, SUTRA_CODE)

	EXAMPLES = [
	('अग्निः', '', 'प.6.3.72: अग्निः'),
		('रामः', '', 'प.6.3.72: रामः'),
		('सीता', '', 'प.6.3.72: सीता'),
	]

