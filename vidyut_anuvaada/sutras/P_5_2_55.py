# Sutra प.5.2.55: त्रेः सम्प्रसारणम् च
# (Strī-pratyaya and taddhita (feminine and secondary derivations)) — treH samprasAraRam ca

from sutra_engines import apply_general

SUTRA_CODE = "प.5.2.55"
SUTRA_TEXT = "त्रेः सम्प्रसारणम् च"
SUTRA_DESC = "(Strī-pratyaya and taddhita (feminine and secondary derivations)) — treH samprasAraRam ca"


class Sutra5255:
	def apply(self, word, pos):
		return apply_general(word, pos, SUTRA_CODE)

	EXAMPLES = [
	('अग्निः', '', 'प.5.2.55: अग्निः'),
		('रामः', '', 'प.5.2.55: रामः'),
		('सीता', '', 'प.5.2.55: सीता'),
	]

