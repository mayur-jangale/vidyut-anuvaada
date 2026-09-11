# Sutra प.5.3.50: षष्ठाष्टमाभ्यां ञ च
# (Strī-pratyaya and taddhita (feminine and secondary derivations)) — zazWAzwamAByAM Ya ca

from sutra_engines import apply_general

SUTRA_CODE = "प.5.3.50"
SUTRA_TEXT = "षष्ठाष्टमाभ्यां ञ च"
SUTRA_DESC = "(Strī-pratyaya and taddhita (feminine and secondary derivations)) — zazWAzwamAByAM Ya ca"


class Sutra5350:
	def apply(self, word, pos):
		return apply_general(word, pos, SUTRA_CODE)

	EXAMPLES = [
	('अग्निः', '', 'प.5.3.50: अग्निः'),
		('रामः', '', 'प.5.3.50: रामः'),
		('सीता', '', 'प.5.3.50: सीता'),
	]

