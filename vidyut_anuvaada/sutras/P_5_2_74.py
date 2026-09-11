# Sutra प.5.2.74: अनुकाभिकाभीकः कमिता
# (Strī-pratyaya and taddhita (feminine and secondary derivations)) — anukABikABIkaH kamitA

from sutra_engines import apply_general

SUTRA_CODE = "प.5.2.74"
SUTRA_TEXT = "अनुकाभिकाभीकः कमिता"
SUTRA_DESC = "(Strī-pratyaya and taddhita (feminine and secondary derivations)) — anukABikABIkaH kamitA"


class Sutra5274:
	def apply(self, word, pos):
		return apply_general(word, pos, SUTRA_CODE)

	EXAMPLES = [
	('अग्निः', '', 'प.5.2.74: अग्निः'),
		('रामः', '', 'प.5.2.74: रामः'),
		('सीता', '', 'प.5.2.74: सीता'),
	]

