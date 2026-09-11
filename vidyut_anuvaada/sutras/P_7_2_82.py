# Sutra प.7.2.82: आने मुक्
# (Taddhita (secondary derivations)) — Ane muk

from sutra_engines import apply_general

SUTRA_CODE = "प.7.2.82"
SUTRA_TEXT = "आने मुक्"
SUTRA_DESC = "(Taddhita (secondary derivations)) — Ane muk"


class Sutra7282:
	def apply(self, word, pos):
		return apply_general(word, pos, SUTRA_CODE)

	EXAMPLES = [
	('अग्निः', '', 'प.7.2.82: अग्निः'),
		('रामः', '', 'प.7.2.82: रामः'),
		('सीता', '', 'प.7.2.82: सीता'),
	]

