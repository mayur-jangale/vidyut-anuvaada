# Sutra प.6.3.27: ईदग्नेः सोमवरुणयोः
# final-sandhi — continued

from sutra_engines import apply_general

SUTRA_CODE = "प.6.3.27"
SUTRA_TEXT = "ईदग्नेः सोमवरुणयोः"
SUTRA_DESC = "final-sandhi — continued"


class Sutra6327:
	def apply(self, word, pos):
		return apply_general(word, pos, SUTRA_CODE)

	EXAMPLES = [
	('अग्निः', '', 'प.6.3.27: अग्निः'),
		('रामः', '', 'प.6.3.27: रामः'),
		('सीता', '', 'प.6.3.27: सीता'),
	]

