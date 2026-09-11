# Sutra प.7.1.78: नाभ्यस्ताच्छतुः
# (Taddhita (secondary derivations)) — nAByastAcCatuH

from sutra_engines import apply_general

SUTRA_CODE = "प.7.1.78"
SUTRA_TEXT = "नाभ्यस्ताच्छतुः"
SUTRA_DESC = "(Taddhita (secondary derivations)) — nAByastAcCatuH"


class Sutra7178:
	def apply(self, word, pos):
		return apply_general(word, pos, SUTRA_CODE)

	EXAMPLES = [
	('अग्निः', '', 'प.7.1.78: अग्निः'),
		('रामः', '', 'प.7.1.78: रामः'),
		('सीता', '', 'प.7.1.78: सीता'),
	]

