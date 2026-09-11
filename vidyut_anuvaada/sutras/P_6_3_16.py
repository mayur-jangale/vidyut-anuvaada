# Sutra प.6.3.16: विभाषा वर्षक्षरशरवरात्
# final-sandhi — continued

from sutra_engines import apply_general

SUTRA_CODE = "प.6.3.16"
SUTRA_TEXT = "विभाषा वर्षक्षरशरवरात्"
SUTRA_DESC = "final-sandhi — continued"


class Sutra6316:
	def apply(self, word, pos):
		return apply_general(word, pos, SUTRA_CODE)

	EXAMPLES = [
	('अग्निः', '', 'प.6.3.16: अग्निः'),
		('रामः', '', 'प.6.3.16: रामः'),
		('सीता', '', 'प.6.3.16: सीता'),
	]

