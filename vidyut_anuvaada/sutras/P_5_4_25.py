# Sutra प.5.4.25: पादार्घाभ्यां च
# (Strī-pratyaya and taddhita (feminine and secondary derivations)) — pAdArGAByAM ca

from sutra_engines import apply_general

SUTRA_CODE = "प.5.4.25"
SUTRA_TEXT = "पादार्घाभ्यां च"
SUTRA_DESC = "(Strī-pratyaya and taddhita (feminine and secondary derivations)) — pAdArGAByAM ca"


class Sutra5425:
	def apply(self, word, pos):
		return apply_general(word, pos, SUTRA_CODE)

	EXAMPLES = [
	('अग्निः', '', 'प.5.4.25: अग्निः'),
		('रामः', '', 'प.5.4.25: रामः'),
		('सीता', '', 'प.5.4.25: सीता'),
	]

