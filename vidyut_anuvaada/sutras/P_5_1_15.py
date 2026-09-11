# Sutra प.5.1.15: चर्मणोऽञ्
# (Strī-pratyaya and taddhita (feminine and secondary derivations)) — carmaRo'Y

from sutra_engines import apply_general

SUTRA_CODE = "प.5.1.15"
SUTRA_TEXT = "चर्मणोऽञ्"
SUTRA_DESC = "(Strī-pratyaya and taddhita (feminine and secondary derivations)) — carmaRo'Y"


class Sutra5115:
	def apply(self, word, pos):
		return apply_general(word, pos, SUTRA_CODE)

	EXAMPLES = [
	('अग्निः', '', 'प.5.1.15: अग्निः'),
		('रामः', '', 'प.5.1.15: रामः'),
		('सीता', '', 'प.5.1.15: सीता'),
	]

