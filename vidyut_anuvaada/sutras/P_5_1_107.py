# Sutra प.5.1.107: कालाद्यत्
# (Strī-pratyaya and taddhita (feminine and secondary derivations)) — kAlAdyat

from sutra_engines import apply_general

SUTRA_CODE = "प.5.1.107"
SUTRA_TEXT = "कालाद्यत्"
SUTRA_DESC = "(Strī-pratyaya and taddhita (feminine and secondary derivations)) — kAlAdyat"


class Sutra51107:
	def apply(self, word, pos):
		return apply_general(word, pos, SUTRA_CODE)

	EXAMPLES = [
	('अग्निः', '', 'प.5.1.107: अग्निः'),
		('रामः', '', 'प.5.1.107: रामः'),
		('सीता', '', 'प.5.1.107: सीता'),
	]

