# Sutra प.8.2.31: हो ढः
# samāse'nañpūrve ktvo lyap — lyap after ktvā in non-negative compounds

from sutra_engines import apply_general

SUTRA_CODE = "प.8.2.31"
SUTRA_TEXT = "हो ढः"
SUTRA_DESC = "samāse'nañpūrve ktvo lyap — lyap after ktvā in non-negative compounds"


class Sutra8231:
	def apply(self, word, pos):
		return apply_general(word, pos, SUTRA_CODE)

	EXAMPLES = [
	('अग्निः', '', 'प.8.2.31: अग्निः'),
		('रामः', '', 'प.8.2.31: रामः'),
		('सीता', '', 'प.8.2.31: सीता'),
	]

