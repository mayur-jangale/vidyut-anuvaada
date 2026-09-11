# Sutra प.5.3.40: अस्ताति च
# (Strī-pratyaya and taddhita (feminine and secondary derivations)) — astAti ca

from sutra_engines import apply_general

SUTRA_CODE = "प.5.3.40"
SUTRA_TEXT = "अस्ताति च"
SUTRA_DESC = "(Strī-pratyaya and taddhita (feminine and secondary derivations)) — astAti ca"


class Sutra5340:
	def apply(self, word, pos):
		return apply_general(word, pos, SUTRA_CODE)

	EXAMPLES = [
	('अग्निः', '', 'प.5.3.40: अग्निः'),
		('रामः', '', 'प.5.3.40: रामः'),
		('सीता', '', 'प.5.3.40: सीता'),
	]

