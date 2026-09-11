# Sutra प.7.3.65: ण्य आवश्यके
# (Taddhita (secondary derivations)) — Rya AvaSyake

from sutra_engines import apply_general

SUTRA_CODE = "प.7.3.65"
SUTRA_TEXT = "ण्य आवश्यके"
SUTRA_DESC = "(Taddhita (secondary derivations)) — Rya AvaSyake"


class Sutra7365:
	def apply(self, word, pos):
		return apply_general(word, pos, SUTRA_CODE)

	EXAMPLES = [
	('अग्निः', '', 'प.7.3.65: अग्निः'),
		('रामः', '', 'प.7.3.65: रामः'),
		('सीता', '', 'प.7.3.65: सीता'),
	]

