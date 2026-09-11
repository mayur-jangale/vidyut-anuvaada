# Sutra प.7.1.11: नेदमदसोरकोः
# (Taddhita (secondary derivations)) — nedamadasorakoH

from sutra_engines import apply_general

SUTRA_CODE = "प.7.1.11"
SUTRA_TEXT = "नेदमदसोरकोः"
SUTRA_DESC = "(Taddhita (secondary derivations)) — nedamadasorakoH"


class Sutra7111:
	def apply(self, word, pos):
		return apply_general(word, pos, SUTRA_CODE)

	EXAMPLES = [
	('अग्निः', '', 'प.7.1.11: अग्निः'),
		('रामः', '', 'प.7.1.11: रामः'),
		('सीता', '', 'प.7.1.11: सीता'),
	]

