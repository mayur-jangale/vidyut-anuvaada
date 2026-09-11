# Sutra प.7.2.32: अपरिह्वृताश्च
# (Taddhita (secondary derivations)) — aparihvftASca

from sutra_engines import apply_general

SUTRA_CODE = "प.7.2.32"
SUTRA_TEXT = "अपरिह्वृताश्च"
SUTRA_DESC = "(Taddhita (secondary derivations)) — aparihvftASca"


class Sutra7232:
	def apply(self, word, pos):
		return apply_general(word, pos, SUTRA_CODE)

	EXAMPLES = [
	('अग्निः', '', 'प.7.2.32: अग्निः'),
		('रामः', '', 'प.7.2.32: रामः'),
		('सीता', '', 'प.7.2.32: सीता'),
	]

