# Sutra प.5.4.128: द्विदण्ड्यादिभ्यश्च
# (Strī-pratyaya and taddhita (feminine and secondary derivations)) — dvidaRqyAdiByaSca

from sutra_engines import apply_general

SUTRA_CODE = "प.5.4.128"
SUTRA_TEXT = "द्विदण्ड्यादिभ्यश्च"
SUTRA_DESC = "(Strī-pratyaya and taddhita (feminine and secondary derivations)) — dvidaRqyAdiByaSca"


class Sutra54128:
	def apply(self, word, pos):
		return apply_general(word, pos, SUTRA_CODE)

	EXAMPLES = [
	('अग्निः', '', 'प.5.4.128: अग्निः'),
		('रामः', '', 'प.5.4.128: रामः'),
		('सीता', '', 'प.5.4.128: सीता'),
	]

