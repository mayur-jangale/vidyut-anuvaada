# Sutra प.7.1.31: पञ्चम्या अत्
# (Taddhita (secondary derivations)) — paYcamyA at

from sutra_engines import apply_general

SUTRA_CODE = "प.7.1.31"
SUTRA_TEXT = "पञ्चम्या अत्"
SUTRA_DESC = "(Taddhita (secondary derivations)) — paYcamyA at"


class Sutra7131:
	def apply(self, word, pos):
		return apply_general(word, pos, SUTRA_CODE)

	EXAMPLES = [
	('अग्निः', '', 'प.7.1.31: अग्निः'),
		('रामः', '', 'प.7.1.31: रामः'),
		('सीता', '', 'प.7.1.31: सीता'),
	]

