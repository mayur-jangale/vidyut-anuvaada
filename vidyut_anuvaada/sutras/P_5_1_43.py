# Sutra प.5.1.43: तत्र विदित इति च
# (Strī-pratyaya and taddhita (feminine and secondary derivations)) — tatra vidita iti ca

from sutra_engines import apply_general

SUTRA_CODE = "प.5.1.43"
SUTRA_TEXT = "तत्र विदित इति च"
SUTRA_DESC = "(Strī-pratyaya and taddhita (feminine and secondary derivations)) — tatra vidita iti ca"


class Sutra5143:
	def apply(self, word, pos):
		return apply_general(word, pos, SUTRA_CODE)

	EXAMPLES = [
	('अग्निः', '', 'प.5.1.43: अग्निः'),
		('रामः', '', 'प.5.1.43: रामः'),
		('सीता', '', 'प.5.1.43: सीता'),
	]

