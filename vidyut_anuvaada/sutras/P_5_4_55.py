# Sutra प.5.4.55: देये त्रा च
# (Strī-pratyaya and taddhita (feminine and secondary derivations)) — deye trA ca

from sutra_engines import apply_general

SUTRA_CODE = "प.5.4.55"
SUTRA_TEXT = "देये त्रा च"
SUTRA_DESC = "(Strī-pratyaya and taddhita (feminine and secondary derivations)) — deye trA ca"


class Sutra5455:
	def apply(self, word, pos):
		return apply_general(word, pos, SUTRA_CODE)

	EXAMPLES = [
	('अग्निः', '', 'प.5.4.55: अग्निः'),
		('रामः', '', 'प.5.4.55: रामः'),
		('सीता', '', 'प.5.4.55: सीता'),
	]

