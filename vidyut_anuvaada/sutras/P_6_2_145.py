# Sutra प.6.2.145: सूपमानात् क्तः
# (Sandhi (euphonic combination)) — sUpamAnAt ktaH

from sutra_engines import apply_general

SUTRA_CODE = "प.6.2.145"
SUTRA_TEXT = "सूपमानात् क्तः"
SUTRA_DESC = "(Sandhi (euphonic combination)) — sUpamAnAt ktaH"


class Sutra62145:
	def apply(self, word, pos):
		return apply_general(word, pos, SUTRA_CODE)

	EXAMPLES = [
	('अग्निः', '', 'प.6.2.145: अग्निः'),
		('रामः', '', 'प.6.2.145: रामः'),
		('सीता', '', 'प.6.2.145: सीता'),
	]

