# Sutra प.5.1.54: द्विगोः ष्ठंश्च
# (Strī-pratyaya and taddhita (feminine and secondary derivations)) — dvigoH zWaMSca

from sutra_engines import apply_general

SUTRA_CODE = "प.5.1.54"
SUTRA_TEXT = "द्विगोः ष्ठंश्च"
SUTRA_DESC = "(Strī-pratyaya and taddhita (feminine and secondary derivations)) — dvigoH zWaMSca"


class Sutra5154:
	def apply(self, word, pos):
		return apply_general(word, pos, SUTRA_CODE)

	EXAMPLES = [
	('अग्निः', '', 'प.5.1.54: अग्निः'),
		('रामः', '', 'प.5.1.54: रामः'),
		('सीता', '', 'प.5.1.54: सीता'),
	]

