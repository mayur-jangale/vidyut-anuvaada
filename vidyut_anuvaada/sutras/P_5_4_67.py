# Sutra प.5.4.67: मद्रात् परिवापणे
# (Strī-pratyaya and taddhita (feminine and secondary derivations)) — madrAt parivApaRe

from sutra_engines import apply_general

SUTRA_CODE = "प.5.4.67"
SUTRA_TEXT = "मद्रात् परिवापणे"
SUTRA_DESC = "(Strī-pratyaya and taddhita (feminine and secondary derivations)) — madrAt parivApaRe"


class Sutra5467:
	def apply(self, word, pos):
		return apply_general(word, pos, SUTRA_CODE)

	EXAMPLES = [
	('अग्निः', '', 'प.5.4.67: अग्निः'),
		('रामः', '', 'प.5.4.67: रामः'),
		('सीता', '', 'प.5.4.67: सीता'),
	]

