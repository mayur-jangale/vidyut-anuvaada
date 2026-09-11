# Sutra प.7.3.75: ष्ठिवुक्लमुचमां शिति
# (Taddhita (secondary derivations)) — zWivuklamucamAM Siti

from sutra_engines import apply_general

SUTRA_CODE = "प.7.3.75"
SUTRA_TEXT = "ष्ठिवुक्लमुचमां शिति"
SUTRA_DESC = "(Taddhita (secondary derivations)) — zWivuklamucamAM Siti"


class Sutra7375:
	def apply(self, word, pos):
		return apply_general(word, pos, SUTRA_CODE)

	EXAMPLES = [
	('अग्निः', '', 'प.7.3.75: अग्निः'),
		('रामः', '', 'प.7.3.75: रामः'),
		('सीता', '', 'प.7.3.75: सीता'),
	]

