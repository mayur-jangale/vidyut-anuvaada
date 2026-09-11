# Sutra प.5.2.99: फेनादिलच् च
# (Strī-pratyaya and taddhita (feminine and secondary derivations)) — PenAdilac ca

from sutra_engines import apply_general

SUTRA_CODE = "प.5.2.99"
SUTRA_TEXT = "फेनादिलच् च"
SUTRA_DESC = "(Strī-pratyaya and taddhita (feminine and secondary derivations)) — PenAdilac ca"


class Sutra5299:
	def apply(self, word, pos):
		return apply_general(word, pos, SUTRA_CODE)

	EXAMPLES = [
	('अग्निः', '', 'प.5.2.99: अग्निः'),
		('रामः', '', 'प.5.2.99: रामः'),
		('सीता', '', 'प.5.2.99: सीता'),
	]

