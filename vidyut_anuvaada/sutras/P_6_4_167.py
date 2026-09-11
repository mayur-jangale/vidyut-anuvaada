# Sutra प.6.4.167: अन्
# (Sandhi (euphonic combination)) — an

from sutra_engines import apply_general

SUTRA_CODE = "प.6.4.167"
SUTRA_TEXT = "अन्"
SUTRA_DESC = "(Sandhi (euphonic combination)) — an"


class Sutra64167:
	def apply(self, word, pos):
		return apply_general(word, pos, SUTRA_CODE)

	EXAMPLES = [
	('अग्निः', '', 'प.6.4.167: अग्निः'),
		('रामः', '', 'प.6.4.167: रामः'),
		('सीता', '', 'प.6.4.167: सीता'),
	]

