# Sutra प.5.4.33: कालाच्च
# (Strī-pratyaya and taddhita (feminine and secondary derivations)) — kAlAcca

from sutra_engines import apply_general

SUTRA_CODE = "प.5.4.33"
SUTRA_TEXT = "कालाच्च"
SUTRA_DESC = "(Strī-pratyaya and taddhita (feminine and secondary derivations)) — kAlAcca"


class Sutra5433:
	def apply(self, word, pos):
		return apply_general(word, pos, SUTRA_CODE)

	EXAMPLES = [
	('अग्निः', '', 'प.5.4.33: अग्निः'),
		('रामः', '', 'प.5.4.33: रामः'),
		('सीता', '', 'प.5.4.33: सीता'),
	]

