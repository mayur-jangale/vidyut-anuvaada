# Sutra प.6.3.104: का पथ्यक्षयोः
# final-sandhi — continued

from sutra_engines import apply_general

SUTRA_CODE = "प.6.3.104"
SUTRA_TEXT = "का पथ्यक्षयोः"
SUTRA_DESC = "final-sandhi — continued"


class Sutra63104:
	def apply(self, word, pos):
		return apply_general(word, pos, SUTRA_CODE)

	EXAMPLES = [
	('अग्निः', '', 'प.6.3.104: अग्निः'),
		('रामः', '', 'प.6.3.104: रामः'),
		('सीता', '', 'प.6.3.104: सीता'),
	]

