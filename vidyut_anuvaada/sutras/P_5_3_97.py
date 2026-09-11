# Sutra प.5.3.97: संज्ञायां च
# (Strī-pratyaya and taddhita (feminine and secondary derivations)) — saMjYAyAM ca

from sutra_engines import apply_general

SUTRA_CODE = "प.5.3.97"
SUTRA_TEXT = "संज्ञायां च"
SUTRA_DESC = "(Strī-pratyaya and taddhita (feminine and secondary derivations)) — saMjYAyAM ca"


class Sutra5397:
	def apply(self, word, pos):
		return apply_general(word, pos, SUTRA_CODE)

	EXAMPLES = [
	('अग्निः', '', 'प.5.3.97: अग्निः'),
		('रामः', '', 'प.5.3.97: रामः'),
		('सीता', '', 'प.5.3.97: सीता'),
	]

