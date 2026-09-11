# Sutra प.6.2.179: अन्तः
# (Sandhi (euphonic combination)) — antaH

from sutra_engines import apply_general

SUTRA_CODE = "प.6.2.179"
SUTRA_TEXT = "अन्तः"
SUTRA_DESC = "(Sandhi (euphonic combination)) — antaH"


class Sutra62179:
	def apply(self, word, pos):
		return apply_general(word, pos, SUTRA_CODE)

	EXAMPLES = [
	('अग्निः', '', 'प.6.2.179: अग्निः'),
		('रामः', '', 'प.6.2.179: रामः'),
		('सीता', '', 'प.6.2.179: सीता'),
	]

