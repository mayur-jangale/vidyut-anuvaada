# Sutra प.6.3.13: बन्धे च विभाषा
# final-sandhi — continued

from sutra_engines import apply_general

SUTRA_CODE = "प.6.3.13"
SUTRA_TEXT = "बन्धे च विभाषा"
SUTRA_DESC = "final-sandhi — continued"


class Sutra6313:
	def apply(self, word, pos):
		return apply_general(word, pos, SUTRA_CODE)

	EXAMPLES = [
	('अग्निः', '', 'प.6.3.13: अग्निः'),
		('रामः', '', 'प.6.3.13: रामः'),
		('सीता', '', 'प.6.3.13: सीता'),
	]

