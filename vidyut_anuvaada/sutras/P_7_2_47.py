# Sutra प.7.2.47: इण्निष्ठायाम्
# (Taddhita (secondary derivations)) — iRnizWAyAm

from sutra_engines import apply_general

SUTRA_CODE = "प.7.2.47"
SUTRA_TEXT = "इण्निष्ठायाम्"
SUTRA_DESC = "(Taddhita (secondary derivations)) — iRnizWAyAm"


class Sutra7247:
	def apply(self, word, pos):
		return apply_general(word, pos, SUTRA_CODE)

	EXAMPLES = [
	('अग्निः', '', 'प.7.2.47: अग्निः'),
		('रामः', '', 'प.7.2.47: रामः'),
		('सीता', '', 'प.7.2.47: सीता'),
	]

