# Sutra प.7.2.87: द्वितीयायां च
# (Taddhita (secondary derivations)) — dvitIyAyAM ca

from sutra_engines import apply_general

SUTRA_CODE = "प.7.2.87"
SUTRA_TEXT = "द्वितीयायां च"
SUTRA_DESC = "(Taddhita (secondary derivations)) — dvitIyAyAM ca"


class Sutra7287:
	def apply(self, word, pos):
		return apply_general(word, pos, SUTRA_CODE)

	EXAMPLES = [
	('अग्निः', '', 'प.7.2.87: अग्निः'),
		('रामः', '', 'प.7.2.87: रामः'),
		('सीता', '', 'प.7.2.87: सीता'),
	]

