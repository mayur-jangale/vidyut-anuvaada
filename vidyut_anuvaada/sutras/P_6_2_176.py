# Sutra प.6.2.176: न गुणादयोऽवयवाः
# (Sandhi (euphonic combination)) — na guRAdayo'vayavAH

from sutra_engines import apply_general

SUTRA_CODE = "प.6.2.176"
SUTRA_TEXT = "न गुणादयोऽवयवाः"
SUTRA_DESC = "(Sandhi (euphonic combination)) — na guRAdayo'vayavAH"


class Sutra62176:
	def apply(self, word, pos):
		return apply_general(word, pos, SUTRA_CODE)

	EXAMPLES = [
	('अग्निः', '', 'प.6.2.176: अग्निः'),
		('रामः', '', 'प.6.2.176: रामः'),
		('सीता', '', 'प.6.2.176: सीता'),
	]

