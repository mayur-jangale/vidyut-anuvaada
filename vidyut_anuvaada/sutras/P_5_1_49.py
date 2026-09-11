# Sutra प.5.1.49: भागाद्यच्च
# (Strī-pratyaya and taddhita (feminine and secondary derivations)) — BAgAdyacca

from sutra_engines import apply_general

SUTRA_CODE = "प.5.1.49"
SUTRA_TEXT = "भागाद्यच्च"
SUTRA_DESC = "(Strī-pratyaya and taddhita (feminine and secondary derivations)) — BAgAdyacca"


class Sutra5149:
	def apply(self, word, pos):
		return apply_general(word, pos, SUTRA_CODE)

	EXAMPLES = [
	('अग्निः', '', 'प.5.1.49: अग्निः'),
		('रामः', '', 'प.5.1.49: रामः'),
		('सीता', '', 'प.5.1.49: सीता'),
	]

