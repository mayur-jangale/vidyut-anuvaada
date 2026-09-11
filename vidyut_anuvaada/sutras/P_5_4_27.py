# Sutra प.5.4.27: देवात्तल्
# (Strī-pratyaya and taddhita (feminine and secondary derivations)) — devAttal

from sutra_engines import apply_general

SUTRA_CODE = "प.5.4.27"
SUTRA_TEXT = "देवात्तल्"
SUTRA_DESC = "(Strī-pratyaya and taddhita (feminine and secondary derivations)) — devAttal"


class Sutra5427:
	def apply(self, word, pos):
		return apply_general(word, pos, SUTRA_CODE)

	EXAMPLES = [
	('अग्निः', '', 'प.5.4.27: अग्निः'),
		('रामः', '', 'प.5.4.27: रामः'),
		('सीता', '', 'प.5.4.27: सीता'),
	]

