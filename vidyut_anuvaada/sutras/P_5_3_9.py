# Sutra प.5.3.9: पर्यभिभ्यां च
# (Strī-pratyaya and taddhita (feminine and secondary derivations)) — paryaBiByAM ca

from sutra_engines import apply_general

SUTRA_CODE = "प.5.3.9"
SUTRA_TEXT = "पर्यभिभ्यां च"
SUTRA_DESC = "(Strī-pratyaya and taddhita (feminine and secondary derivations)) — paryaBiByAM ca"


class Sutra539:
	def apply(self, word, pos):
		return apply_general(word, pos, SUTRA_CODE)

	EXAMPLES = [
	('अग्निः', '', 'प.5.3.9: अग्निः'),
		('रामः', '', 'प.5.3.9: रामः'),
		('सीता', '', 'प.5.3.9: सीता'),
	]

