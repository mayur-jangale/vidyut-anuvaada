# Sutra प.7.1.50: आज्जसेरसुक्
# (Taddhita (secondary derivations)) — Ajjaserasuk

from sutra_engines import apply_general

SUTRA_CODE = "प.7.1.50"
SUTRA_TEXT = "आज्जसेरसुक्"
SUTRA_DESC = "(Taddhita (secondary derivations)) — Ajjaserasuk"


class Sutra7150:
	def apply(self, word, pos):
		return apply_general(word, pos, SUTRA_CODE)

	EXAMPLES = [
	('अग्निः', '', 'प.7.1.50: अग्निः'),
		('रामः', '', 'प.7.1.50: रामः'),
		('सीता', '', 'प.7.1.50: सीता'),
	]

