# Sutra प.5.3.54: षष्ठ्या रूप्य च
# (Strī-pratyaya and taddhita (feminine and secondary derivations)) — zazWyA rUpya ca

from sutra_engines import apply_general

SUTRA_CODE = "प.5.3.54"
SUTRA_TEXT = "षष्ठ्या रूप्य च"
SUTRA_DESC = "(Strī-pratyaya and taddhita (feminine and secondary derivations)) — zazWyA rUpya ca"


class Sutra5354:
	def apply(self, word, pos):
		return apply_general(word, pos, SUTRA_CODE)

	EXAMPLES = [
	('अग्निः', '', 'प.5.3.54: अग्निः'),
		('रामः', '', 'प.5.3.54: रामः'),
		('सीता', '', 'प.5.3.54: सीता'),
	]

