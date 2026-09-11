# Sutra प.6.3.97: द्व्यन्तरुपसर्गेभ्योऽप ईत्
# final-sandhi — continued

from sutra_engines import apply_general

SUTRA_CODE = "प.6.3.97"
SUTRA_TEXT = "द्व्यन्तरुपसर्गेभ्योऽप ईत्"
SUTRA_DESC = "final-sandhi — continued"


class Sutra6397:
	def apply(self, word, pos):
		return apply_general(word, pos, SUTRA_CODE)

	EXAMPLES = [
	('अग्निः', '', 'प.6.3.97: अग्निः'),
		('रामः', '', 'प.6.3.97: रामः'),
		('सीता', '', 'प.6.3.97: सीता'),
	]

