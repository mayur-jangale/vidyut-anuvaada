# Sutra प.8.4.65: झरो झरि सवर्णे
# final transformations — continued

from sutra_engines import apply_general

SUTRA_CODE = "प.8.4.65"
SUTRA_TEXT = "झरो झरि सवर्णे"
SUTRA_DESC = "final transformations — continued"


class Sutra8465:
	def apply(self, word, pos):
		return apply_general(word, pos, SUTRA_CODE)

	EXAMPLES = [
	('अग्निः', '', 'प.8.4.65: अग्निः'),
		('रामः', '', 'प.8.4.65: रामः'),
		('सीता', '', 'प.8.4.65: सीता'),
	]

