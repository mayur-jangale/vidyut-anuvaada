# Sutra प.5.2.67: उदराट्ठगाद्यूने
# (Strī-pratyaya and taddhita (feminine and secondary derivations)) — udarAwWagAdyUne

from sutra_engines import apply_general

SUTRA_CODE = "प.5.2.67"
SUTRA_TEXT = "उदराट्ठगाद्यूने"
SUTRA_DESC = "(Strī-pratyaya and taddhita (feminine and secondary derivations)) — udarAwWagAdyUne"


class Sutra5267:
	def apply(self, word, pos):
		return apply_general(word, pos, SUTRA_CODE)

	EXAMPLES = [
	('अग्निः', '', 'प.5.2.67: अग्निः'),
		('रामः', '', 'प.5.2.67: रामः'),
		('सीता', '', 'प.5.2.67: सीता'),
	]

