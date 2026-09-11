# Sutra प.6.2.101: न हास्तिनफलकमार्देयाः
# (Sandhi (euphonic combination)) — na hAstinaPalakamArdeyAH

from sutra_engines import apply_general

SUTRA_CODE = "प.6.2.101"
SUTRA_TEXT = "न हास्तिनफलकमार्देयाः"
SUTRA_DESC = "(Sandhi (euphonic combination)) — na hAstinaPalakamArdeyAH"


class Sutra62101:
	def apply(self, word, pos):
		return apply_general(word, pos, SUTRA_CODE)

	EXAMPLES = [
	('अग्निः', '', 'प.6.2.101: अग्निः'),
		('रामः', '', 'प.6.2.101: रामः'),
		('सीता', '', 'प.6.2.101: सीता'),
	]

