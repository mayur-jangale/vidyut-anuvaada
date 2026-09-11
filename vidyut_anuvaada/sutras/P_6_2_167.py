# Sutra प.6.2.167: मुखं स्वाङ्गम्
# (Sandhi (euphonic combination)) — muKaM svANgam

from sutra_engines import apply_general

SUTRA_CODE = "प.6.2.167"
SUTRA_TEXT = "मुखं स्वाङ्गम्"
SUTRA_DESC = "(Sandhi (euphonic combination)) — muKaM svANgam"


class Sutra62167:
	def apply(self, word, pos):
		return apply_general(word, pos, SUTRA_CODE)

	EXAMPLES = [
	('अग्निः', '', 'प.6.2.167: अग्निः'),
		('रामः', '', 'प.6.2.167: रामः'),
		('सीता', '', 'प.6.2.167: सीता'),
	]

