# Sutra प.5.1.100: कर्मवेषाद्यत्
# (Strī-pratyaya and taddhita (feminine and secondary derivations)) — karmavezAdyat

from sutra_engines import apply_general

SUTRA_CODE = "प.5.1.100"
SUTRA_TEXT = "कर्मवेषाद्यत्"
SUTRA_DESC = "(Strī-pratyaya and taddhita (feminine and secondary derivations)) — karmavezAdyat"


class Sutra51100:
	def apply(self, word, pos):
		return apply_general(word, pos, SUTRA_CODE)

	EXAMPLES = [
	('अग्निः', '', 'प.5.1.100: अग्निः'),
		('रामः', '', 'प.5.1.100: रामः'),
		('सीता', '', 'प.5.1.100: सीता'),
	]

