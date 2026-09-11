# Sutra प.5.3.46: एधाच्च
# (Strī-pratyaya and taddhita (feminine and secondary derivations)) — eDAcca

from sutra_engines import apply_general

SUTRA_CODE = "प.5.3.46"
SUTRA_TEXT = "एधाच्च"
SUTRA_DESC = "(Strī-pratyaya and taddhita (feminine and secondary derivations)) — eDAcca"


class Sutra5346:
	def apply(self, word, pos):
		return apply_general(word, pos, SUTRA_CODE)

	EXAMPLES = [
	('अग्निः', '', 'प.5.3.46: अग्निः'),
		('रामः', '', 'प.5.3.46: रामः'),
		('सीता', '', 'प.5.3.46: सीता'),
	]

