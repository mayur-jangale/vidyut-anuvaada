# Sutra प.6.2.178: वनं समासे
# (Sandhi (euphonic combination)) — vanaM samAse

from sutra_engines import apply_general

SUTRA_CODE = "प.6.2.178"
SUTRA_TEXT = "वनं समासे"
SUTRA_DESC = "(Sandhi (euphonic combination)) — vanaM samAse"


class Sutra62178:
	def apply(self, word, pos):
		return apply_general(word, pos, SUTRA_CODE)

	EXAMPLES = [
	('अग्निः', '', 'प.6.2.178: अग्निः'),
		('रामः', '', 'प.6.2.178: रामः'),
		('सीता', '', 'प.6.2.178: सीता'),
	]

