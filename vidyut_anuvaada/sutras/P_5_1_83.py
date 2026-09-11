# Sutra प.5.1.83: षण्मासाण्ण्यच्च
# (Strī-pratyaya and taddhita (feminine and secondary derivations)) — zaRmAsARRyacca

from sutra_engines import apply_general

SUTRA_CODE = "प.5.1.83"
SUTRA_TEXT = "षण्मासाण्ण्यच्च"
SUTRA_DESC = "(Strī-pratyaya and taddhita (feminine and secondary derivations)) — zaRmAsARRyacca"


class Sutra5183:
	def apply(self, word, pos):
		return apply_general(word, pos, SUTRA_CODE)

	EXAMPLES = [
	('अग्निः', '', 'प.5.1.83: अग्निः'),
		('रामः', '', 'प.5.1.83: रामः'),
		('सीता', '', 'प.5.1.83: सीता'),
	]

