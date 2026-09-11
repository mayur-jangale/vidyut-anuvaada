# Sutra प.7.1.30: भ्यसो भ्यम्
# (Taddhita (secondary derivations)) — Byaso Byam

from sutra_engines import apply_general

SUTRA_CODE = "प.7.1.30"
SUTRA_TEXT = "भ्यसो भ्यम्"
SUTRA_DESC = "(Taddhita (secondary derivations)) — Byaso Byam"


class Sutra7130:
	def apply(self, word, pos):
		return apply_general(word, pos, SUTRA_CODE)

	EXAMPLES = [
	('अग्निः', '', 'प.7.1.30: अग्निः'),
		('रामः', '', 'प.7.1.30: रामः'),
		('सीता', '', 'प.7.1.30: सीता'),
	]

