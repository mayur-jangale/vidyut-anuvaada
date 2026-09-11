# Sutra प.6.3.14: तत्पुरुषे कृति बहुलम्
# final-sandhi — continued

from sutra_engines import apply_general

SUTRA_CODE = "प.6.3.14"
SUTRA_TEXT = "तत्पुरुषे कृति बहुलम्"
SUTRA_DESC = "final-sandhi — continued"


class Sutra6314:
	def apply(self, word, pos):
		return apply_general(word, pos, SUTRA_CODE)

	EXAMPLES = [
	('अग्निः', '', 'प.6.3.14: अग्निः'),
		('रामः', '', 'प.6.3.14: रामः'),
		('सीता', '', 'प.6.3.14: सीता'),
	]

