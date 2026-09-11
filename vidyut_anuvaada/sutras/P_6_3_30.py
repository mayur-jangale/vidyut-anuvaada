# Sutra प.6.3.30: दिवसश्च पृथिव्याम्
# final-sandhi — continued

from sutra_engines import apply_general

SUTRA_CODE = "प.6.3.30"
SUTRA_TEXT = "दिवसश्च पृथिव्याम्"
SUTRA_DESC = "final-sandhi — continued"


class Sutra6330:
	def apply(self, word, pos):
		return apply_general(word, pos, SUTRA_CODE)

	EXAMPLES = [
	('अग्निः', '', 'प.6.3.30: अग्निः'),
		('रामः', '', 'प.6.3.30: रामः'),
		('सीता', '', 'प.6.3.30: सीता'),
	]

