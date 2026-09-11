# Sutra प.6.2.115: शृङ्गमवस्थायां च
# (Sandhi (euphonic combination)) — SfNgamavasTAyAM ca

from sutra_engines import apply_general

SUTRA_CODE = "प.6.2.115"
SUTRA_TEXT = "शृङ्गमवस्थायां च"
SUTRA_DESC = "(Sandhi (euphonic combination)) — SfNgamavasTAyAM ca"


class Sutra62115:
	def apply(self, word, pos):
		return apply_general(word, pos, SUTRA_CODE)

	EXAMPLES = [
	('अग्निः', '', 'प.6.2.115: अग्निः'),
		('रामः', '', 'प.6.2.115: रामः'),
		('सीता', '', 'प.6.2.115: सीता'),
	]

