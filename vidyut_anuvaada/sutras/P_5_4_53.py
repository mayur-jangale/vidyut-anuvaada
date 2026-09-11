# Sutra प.5.4.53: अभिविधौ सम्पदा च
# (Strī-pratyaya and taddhita (feminine and secondary derivations)) — aBiviDO sampadA ca

from sutra_engines import apply_general

SUTRA_CODE = "प.5.4.53"
SUTRA_TEXT = "अभिविधौ सम्पदा च"
SUTRA_DESC = "(Strī-pratyaya and taddhita (feminine and secondary derivations)) — aBiviDO sampadA ca"


class Sutra5453:
	def apply(self, word, pos):
		return apply_general(word, pos, SUTRA_CODE)

	EXAMPLES = [
	('अग्निः', '', 'प.5.4.53: अग्निः'),
		('रामः', '', 'प.5.4.53: रामः'),
		('सीता', '', 'प.5.4.53: सीता'),
	]

