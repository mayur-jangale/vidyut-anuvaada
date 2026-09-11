# Sutra प.5.2.87: सपूर्वाच्च
# (Strī-pratyaya and taddhita (feminine and secondary derivations)) — sapUrvAcca

from sutra_engines import apply_general

SUTRA_CODE = "प.5.2.87"
SUTRA_TEXT = "सपूर्वाच्च"
SUTRA_DESC = "(Strī-pratyaya and taddhita (feminine and secondary derivations)) — sapUrvAcca"


class Sutra5287:
	def apply(self, word, pos):
		return apply_general(word, pos, SUTRA_CODE)

	EXAMPLES = [
	('अग्निः', '', 'प.5.2.87: अग्निः'),
		('रामः', '', 'प.5.2.87: रामः'),
		('सीता', '', 'प.5.2.87: सीता'),
	]

