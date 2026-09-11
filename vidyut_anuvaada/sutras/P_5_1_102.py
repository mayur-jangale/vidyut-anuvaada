# Sutra प.5.1.102: योगाद्यच्च
# (Strī-pratyaya and taddhita (feminine and secondary derivations)) — yogAdyacca

from sutra_engines import apply_general

SUTRA_CODE = "प.5.1.102"
SUTRA_TEXT = "योगाद्यच्च"
SUTRA_DESC = "(Strī-pratyaya and taddhita (feminine and secondary derivations)) — yogAdyacca"


class Sutra51102:
	def apply(self, word, pos):
		return apply_general(word, pos, SUTRA_CODE)

	EXAMPLES = [
	('अग्निः', '', 'प.5.1.102: अग्निः'),
		('रामः', '', 'प.5.1.102: रामः'),
		('सीता', '', 'प.5.1.102: सीता'),
	]

