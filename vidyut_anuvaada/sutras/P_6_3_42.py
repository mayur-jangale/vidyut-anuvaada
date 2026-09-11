# Sutra प.6.3.42: पुंवत् कर्मधारयजातीयदेशीयेषु
# final-sandhi — continued

from sutra_engines import apply_general

SUTRA_CODE = "प.6.3.42"
SUTRA_TEXT = "पुंवत् कर्मधारयजातीयदेशीयेषु"
SUTRA_DESC = "final-sandhi — continued"


class Sutra6342:
	def apply(self, word, pos):
		return apply_general(word, pos, SUTRA_CODE)

	EXAMPLES = [
	('अग्निः', '', 'प.6.3.42: अग्निः'),
		('रामः', '', 'प.6.3.42: रामः'),
		('सीता', '', 'प.6.3.42: सीता'),
	]

